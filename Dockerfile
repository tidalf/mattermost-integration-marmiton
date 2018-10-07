FROM python:3.6-alpine

MAINTAINER Kyâne PICHOU kyane@kyane.fr

COPY . /mattermost-marmiton
WORKDIR /mattermost-marmiton
RUN apk update && apk upgrade && \
    apk add --no-cache bash git

RUN pip install "git+https://github.com/tidalf/python-marmiton.git"
RUN python3 setup.py install

ENTRYPOINT ["python", "run.py"]
