FROM ubuntu:20.04

MAINTAINER Hugo Perez "vhpvmx@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./r.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
