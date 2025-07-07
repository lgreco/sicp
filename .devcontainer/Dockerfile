FROM mcr.microsoft.com/devcontainers/base:ubuntu

RUN apt-get update \
  && apt-get install -y wget curl unzip \
  && curl -O https://download.racket-lang.org/installers/9.7/racket-9.7-x86_64-linux.sh \
  && chmod +x racket-9.7-x86_64-linux.sh \
  && ./racket-9.7-x86_64-linux.sh --in-place \
  && rm racket-9.7-x86_64-linux.sh \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
