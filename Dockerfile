FROM python:3-slim-bullseye

COPY startup.sh /scripts/startup.sh
COPY hvac-monitor.py /scripts/hvac-monitor.py

RUN apt-get update && \
    apt-get install owserver owfs-fuse -y && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && \
    pip install --no-cache-dir paho-mqtt && \
    rm -rf /root/.cache/pip && \
    mkdir -p /mnt/1wire && \
    mkdir -p /scripts && \
    chmod +x /scripts/startup.sh

ENTRYPOINT [ "/bin/bash", "-c", "/scripts/startup.sh" ]