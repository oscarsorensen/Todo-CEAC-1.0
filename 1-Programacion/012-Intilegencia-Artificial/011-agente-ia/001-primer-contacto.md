NAME                       ID              SIZE      MODIFIED
qwen2.5:3b-instruct        357c53fb659c    1.9 GB    2 weeks ago
qwen2.5:14b-instruct       7cdf5a0187d5    9.0 GB    3 weeks ago
qwen2.5:14b                7cdf5a0187d5    9.0 GB    3 weeks ago
qwen2.5-coder:7b           dae161e27b0e    4.7 GB    6 weeks ago
phi3:latest                4f2222927938    2.2 GB    6 weeks ago
qwen2.5:7b-instruct        845dbda0ea48    4.7 GB    6 weeks ago
llama3:instruct            365c0bd3c000    4.7 GB    6 weeks ago
llama3:8b                  365c0bd3c000    4.7 GB    6 weeks ago
nomic-embed-text:latest    0a109f422b47    274 MB    6 weeks ago


ollama run qwen2.5-coder:7b "crea una web en HTML, sin comentarios, solo el código"

josevicente@josevicenteportatil:~$ ollama run qwen2.5-coder:7b "crea un programa en Python, que sume 4+3. Solo quiero el codigo, ningun comentario."
```python
print(4 + 3)
```