FROM python:3.12-slim

WORKDIR /azure-chat

RUN apt-get update && apt-get -y upgrade

COPY . /azure-chat

# EXPOSE 8501

RUN pip install -r ./requirements.txt