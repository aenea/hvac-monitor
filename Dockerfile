FROM python:3-alpine

COPY startup.sh /scripts/startup.sh
COPY hvac-monitor.py /scripts/hvac-monitor.py

RUN apk add owfs && \
    pip install --upgrade pip && \
    pip install --no-cache-dir paho-mqtt && \
    rm -rf /root/.cache/pip && \
    mkdir -p /mnt/1wire && \
    mkdir -p /scripts && \
    chmod +x /scripts/startup.sh

ENTRYPOINT [ "/bin/sh", "-c", "/scripts/startup.sh" ]