FROM ubuntu:16.04

MAINTAINER Sabdeep Reddy "sandeep.reddy@tigeranalytics.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt
COPY ./pickle_model.pkl /pickle_model.pkl

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
