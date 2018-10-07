FROM python:2.7-alpine

MAINTAINER Kyâne PICHOU kyane@kyane.fr

COPY . /mattermost-marmiton
WORKDIR /mattermost-marmiton

RUN python setup.py install

ENTRYPOINT ["python", "run.py"]
