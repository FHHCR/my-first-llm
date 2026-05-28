import requests
import json

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        "model": "qwen3.5:4b",
        "prompt": "用一句话解释什么是RAG技术",
        "stream": False
    }
)

print(response.json()['response'])