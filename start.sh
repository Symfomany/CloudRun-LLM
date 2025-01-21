#!/bin/bash
export OLLAMA_HOST=0.0.0.0
export OLLAMA_KEEP_ALIVE=-1

ollama pull qwen:2.5-7b-instruct

ollama serve &

# Ready for start
until curl -s http://localhost:11434/api/tags > /dev/null; do
    echo "Waiting for Ollama to start..."
    sleep 2
done

# ollama pull qwen2.5-coder

echo "Starting FastAPI application..."
exec uvicorn main:app --host 0.0.0.0 --port 8080