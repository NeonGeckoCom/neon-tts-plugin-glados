FROM python:3.7

RUN apt-get update -y
RUN apt-get install espeak -y

ADD . /tts_plugin
WORKDIR /tts_plugin

RUN pip install .[docker]

ENTRYPOINT ovos-tts-server --engine neon-tts-plugin-glados --cache