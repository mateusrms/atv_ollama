# atv_ollama

Este projeto tem como objetivo gerar vetores de embeddings a partir de um texto simples utilizando o modelo nomic-embed-text rodando localmente com o Ollama.

Para usar, primeiro instale o Ollama através do site oficial (https://ollama.com/download). Depois, inicie o serviço local com o comando ollama serve. Com o Ollama rodando, baixe o modelo necessário com o comando ollama pull nomic-embed-text.

Em seguida, instale a biblioteca requests com o comando pip install requests. Depois disso, execute o script Python com python gerar_embedding.py. O script enviará um texto ao Ollama, gerará o vetor de embeddings e mostrará parte do resultado no console, incluindo o tamanho do vetor e os primeiros valores.

Requisitos: Python 3.8 ou superior, Ollama instalado e ativo, e o modelo nomic-embed-text baixado.