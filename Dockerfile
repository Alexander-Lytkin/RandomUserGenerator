FROM python:3.11

WORKDIR ./RandomUserGenerator

COPY . /RandomUserGenerator

WORKDIR /RandomUserGenerator

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD pytest --env-cfg=env.dev.yaml test_api/*
