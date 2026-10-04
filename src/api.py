"""Thin cached, threaded OpenRouter client used for rewriting, judging and API responders."""
import hashlib, json, os, threading, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from openai import OpenAI
from tqdm import tqdm

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "results" / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
_client = OpenAI(api_key=os.environ["OPENROUTER_KEY"], base_url="https://openrouter.ai/api/v1", timeout=90, max_retries=0)
_lock = threading.Lock()
_caches = {}
USAGE = {}  # model -> [prompt_tokens, completion_tokens]


def _cache(name):
    if name not in _caches:
        path = CACHE_DIR / f"{name}.jsonl"
        d = {}
        if path.exists():
            for line in open(path):
                try:
                    r = json.loads(line); d[r["k"]] = r["v"]
                except Exception:
                    pass
        _caches[name] = (d, open(path, "a"))
    return _caches[name]


def chat(model, messages, cache="default", max_tokens=1500, temperature=None, reasoning="low", tag=""):
    """One chat completion. Returns text ('' on empty/failed). Cached on (model, messages, params, tag)."""
    key = hashlib.sha256(json.dumps([model, messages, max_tokens, temperature, reasoning, tag]).encode()).hexdigest()
    with _lock:
        d, fh = _cache(cache)
        if key in d:
            return d[key]
    if os.environ.get("API_OFFLINE"):  # cache-only mode (used after the OpenRouter key hit its daily limit)
        return "__API_ERROR__"
    kw = dict(model=model, messages=messages, max_tokens=max_tokens)
    if temperature is not None:
        kw["temperature"] = temperature
    if reasoning:
        kw["extra_body"] = {"reasoning": {"effort": reasoning}}
    out = None
    for attempt in range(4):
        try:
            r = _client.chat.completions.create(**kw)
            if r.choices is None:  # provider-side block (e.g. moderation): retry once, then treat as empty output
                if attempt == 0: continue
                out = ""; break
            out = r.choices[0].message.content or ""
            if r.usage:
                with _lock:
                    u = USAGE.setdefault(model, [0, 0])
                    u[0] += r.usage.prompt_tokens; u[1] += r.usage.completion_tokens
            break
        except Exception as e:  # rate limits / transient errors: back off and retry
            err = str(e); print("API error:", model, err[:200], flush=True)
            time.sleep(min(60, 2 ** attempt * 2))
    if out is None:
        return "__API_ERROR__"  # not cached, so a re-run retries it
    with _lock:
        d[key] = out
        fh.write(json.dumps({"k": key, "v": out}) + "\n"); fh.flush()
    return out


def pmap(fn, items, workers=16, desc=""):
    """Thread-pool map preserving order."""
    with ThreadPoolExecutor(workers) as ex:
        return list(tqdm(ex.map(fn, items), total=len(items), desc=desc, mininterval=10))


def dump_usage(path):
    old = json.load(open(path)) if os.path.exists(path) else {}
    for m, (a, b) in USAGE.items():
        o = old.get(m, [0, 0]); old[m] = [o[0] + a, o[1] + b]
    json.dump(old, open(path, "w"), indent=1)
