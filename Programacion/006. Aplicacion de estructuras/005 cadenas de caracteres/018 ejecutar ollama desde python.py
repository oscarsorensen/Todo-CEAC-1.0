
import requests
import json

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen2.5:3b-instruct",
    "prompt": "Fortæl mig en godnathistorie på dansk",
    "stream": False
}

response = requests.post(url, json=payload)

data = response.json()
print(data["response"])