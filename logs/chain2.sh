#!/bin/bash
cd /workspaces/do-llms-behave-differently-when-4fc5-claude-fable-5-1
source .venv/bin/activate
export TORCH_DISABLE_NATIVE_JIT=1
until [ -f logs/chain.done ]; do sleep 15; done
python src/run_local_free.py llama > logs/run_local_free_llama.log 2>&1
python src/run_local_free.py qwen > logs/run_local_free_qwen.log 2>&1
echo DONE > logs/chain2.done
