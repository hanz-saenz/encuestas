FROM ubuntu:22.04

RUN apt-get update

RUN apt-get install -y python3 python3-pip python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev unzip wget

RUN pip3 install --upgrade pip

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY .. /encuestas

WORKDIR /encuestas

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8001"]