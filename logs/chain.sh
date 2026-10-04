#!/bin/bash
# GPU job chain: llama steering -> qwen stage 1 -> qwen steering
cd /workspaces/do-llms-behave-differently-when-4fc5-claude-fable-5-1
source .venv/bin/activate
export TORCH_DISABLE_NATIVE_JIT=1
python src/run_steer.py llama > logs/run_steer_llama.log 2>&1
python src/run_local.py qwen > logs/run_local_qwen.log 2>&1
python src/run_steer.py qwen > logs/run_steer_qwen.log 2>&1
echo CHAIN_DONE > logs/chain.done
