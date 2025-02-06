FROM mcr.microsoft.com/vscode/devcontainers/python:3.13

WORKDIR /usr/covtscollection

COPY ./requirements.txt ./requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

