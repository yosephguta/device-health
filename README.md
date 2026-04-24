# Device Health Diagnostic Tool

A containerized diagnostic CLI tool that inspects a Linux device and produces 
a human-readable health report plus a compressed bundle for remote debugging.

Inspired by real-world edge device infrastructure (k3s, PipeWire, HDMI kiosks).

## What it checks
- **System** — Disk and RAM usage
- **Network** — Internet connectivity and local IP
- **Kubernetes** — k3s pod health via kubectl
- **Audio** — PipeWire service status via systemctl

## Run it
```bash
docker build -t device-health .
docker run --rm device-health
```

## Output
- Human-readable report printed to terminal
- Compressed `.tar.gz` bundle saved to `/tmp/` for remote debugging

## Stack
- Python 3
- Docker
- psutil, subprocess, tarfile, socket