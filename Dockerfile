FROM python:3.7

RUN apt-get update -y
RUN apt-get install espeak -y

RUN pip3 install ovos-utils==0.0.15
RUN pip3 install ovos-plugin-manager==0.0.4
RUN pip3 install ovos-tts-server==0.0.1

RUN pip3 install git+https://github.com/NeonGeckoCom/neon-tts-plugin-glados


ENTRYPOINT ovos-tts-server --engine neon-tts-plugin-glados --cache