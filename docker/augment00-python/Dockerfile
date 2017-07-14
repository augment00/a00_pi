FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update && \
    apt-get -qy install \
        python python-pip \
        python-dev gcc make git

RUN apt-get install -y python-imaging

RUN pip install rpi.gpio
RUN pip install pycrypto
RUN pip install requests






