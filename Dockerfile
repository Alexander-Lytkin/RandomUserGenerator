FROM python:3.8-slim-buster

WORKDIR ./RandomUserGenerator

COPY . /RandomUserGenerator

WORKDIR /RandomUserGenerator

RUN apt update -y \
    && apt install -y git \
    && apt install -y moreutils libzbar0 libzbar-dev curl libssl-dev libsasl2-dev libldap2-dev wget

COPY requirements.txt /RandomUserGenerator/requirements.txt
RUN pip install -r requirements.txt

CMD pytest --env-cfg=env.dev.yaml test_api/*
