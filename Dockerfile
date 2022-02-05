FROM python:alpine AS base

ENV USER=aibc
ENV HOME=/home/$USER
ENV PROJECT=$HOME/$USER

RUN addgroup -S $USER && adduser -S $USER -G $USER -s /bin/sh
#RUN set -ex && apk --no-cache add sudo
RUN apk --no-cache update &&  \
    apk --no-cache add sudo && \
    echo "%$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

from base as environment

USER $USER
WORKDIR $HOME

COPY --chown=$USER:$USER . $PROJECT

ENV VIRTUAL_ENV=$HOME/venv
# permanently activate venv, see https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python3 -m pip install --upgrade pip
RUN cd $PROJECT && pip install .
