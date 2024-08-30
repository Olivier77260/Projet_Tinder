# Fichier utilisé pour la mise en place de l'application sur mon propre serveur dans un container Docker afin de pérenniser l'utilisation suivant la version des modules.

FROM python:3.9-slim

WORKDIR /var/www/html/streamlit/app


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Olivier77260/Projet_Tinder.git /var/www/html/streamlit/app

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
