import requests

# Texto de entrada
texto = "Este é um exemplo simples de texto para gerar embeddings."

# Requisição para o Ollama local
resposta = requests.post("http://localhost:11434/api/embeddings", json={
    "model": "nomic-embed-text",
    "prompt": texto
})

# Verificando a resposta
if resposta.status_code == 200:
    data = resposta.json()
    embedding = data["embedding"]
    print(f"Embedding gerado com sucesso! Tamanho do vetor: {len(embedding)}")
    print("Primeiros 10 valores:")
    print(embedding[:10])
else:
    print(f"Erro: {resposta.status_code}")
    print(resposta.text)
