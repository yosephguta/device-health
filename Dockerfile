FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install psutil

WORKDIR /workspace
COPY . .

CMD ["python3", "main.py"]