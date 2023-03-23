FROM python:3-slim-bullseye

RUN apt-get update && \
    apt-get install owserver -y && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install paho-mqtt