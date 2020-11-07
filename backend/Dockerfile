FROM python:3.9.0

# バイナリレイヤのバッファリングを解除
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

RUN apt-get -y update \
    && apt-get -y --no-install-recommends install \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install pip-tools==5.3.1 \
    && pip-sync

EXPOSE 8000
