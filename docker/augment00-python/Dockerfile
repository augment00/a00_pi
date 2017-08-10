FROM resin/rpi-raspbian:latest
ENTRYPOINT []

RUN apt-get -q update && apt-get -qy install python-dev gcc make git

RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python2.7

RUN apt-get install -y python-imaging

RUN pip install rpi.gpio
RUN pip install pycrypto
RUN pip install requests
RUN pip install tinkerforge
RUN pip install pillow
RUN pip install rdflib
RUN pip install influxdb
RUN pip install numpy
RUN pip install colour






