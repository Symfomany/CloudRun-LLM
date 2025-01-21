FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install -y curl


WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY main.py .
COPY ./model /model

EXPOSE 8080

# Supprimer la ligne RUN ollama pull
# CMD ollama serve & uvicorn main:app --host 0.0.0.0 --port $PORT
# # CMD ["sh", "-c", "ollama pull qwen:2.5-7b-instruct && ollama serve & uvicorn main:app --host 0.0.0.0 --port $PORT"]

# Copie du script de démarrage
COPY start.sh .
RUN chmod +x start.sh

# Utilisation du script de démarrage
ENTRYPOINT ["./start.sh"]