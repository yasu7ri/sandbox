FROM mcr.microsoft.com/devcontainers/python:0-3.11
RUN apt-get update \
    && apt-get install -y --no-install-recommends libreoffice-impress \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*
