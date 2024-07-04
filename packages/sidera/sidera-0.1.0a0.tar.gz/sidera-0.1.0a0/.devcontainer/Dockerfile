FROM debian:bookworm-slim as builder

WORKDIR /home/vscode

ENV RYE_HOME="/home/vscode/.rye"
ENV PATH="$RYE_HOME/shims:$PATH"

# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]
RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm
COPY --from=builder /home/vscode/.rye /home/vscode/.rye

ENV RYE_HOME="/home/vscode/.rye"
ENV PATH="$RYE_HOME/shims:$PATH"

ENV PYTHONUNBUFFERED True

RUN chown -R vscode $RYE_HOME && chgrp -R vscode $RYE_HOME
