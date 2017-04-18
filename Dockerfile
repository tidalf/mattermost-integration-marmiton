FROM python:2.7

MAINTAINER Kyâne PICHOU kyane@kyane.fr

RUN apt-get update && \
    apt-get install -y \
      python-pip \
      python-dev \
      build-essential && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

COPY . /mattermost-giphy
WORKDIR /mattermost-giphy

RUN python setup.py install

ENTRYPOINT ["python", "run.py"]
