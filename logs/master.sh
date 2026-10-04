#!/bin/bash
# Serial GPU queue (one process on the GPU at a time).
cd /workspaces/do-llms-behave-differently-when-4fc5-claude-fable-5-1
source .venv/bin/activate
export TORCH_DISABLE_NATIVE_JIT=1
J="python src/local_judge.py label llama"
until grep -q "^done" logs/run_steer_llama.log; do sleep 15; done
sleep 20
$J results/llama/steer_raw.jsonl results/llama/steer_judged_local.jsonl > logs/lj_steer_llama.log 2>&1
$J results/gemini/behaviour_raw.jsonl results/gemini/behaviour_judged.jsonl > logs/lj_gemini.log 2>&1
python src/run_local.py qwen > logs/run_local_qwen.log 2>&1
$J results/qwen/behaviour_raw.jsonl results/qwen/behaviour_judged.jsonl > logs/lj_qwen.log 2>&1
python src/run_local_free.py llama > logs/run_local_free_llama.log 2>&1
$J results/llama/free_raw.jsonl results/llama/free_judged.jsonl > logs/lj_free_llama.log 2>&1
python src/run_steer.py qwen > logs/run_steer_qwen.log 2>&1
$J results/qwen/steer_raw.jsonl results/qwen/steer_judged_local.jsonl > logs/lj_steer_qwen.log 2>&1
python src/run_local_free.py qwen > logs/run_local_free_qwen.log 2>&1
$J results/qwen/free_raw.jsonl results/qwen/free_judged.jsonl > logs/lj_free_qwen.log 2>&1
echo DONE > logs/master.done
