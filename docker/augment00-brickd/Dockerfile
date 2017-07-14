FROM paulharter/augment00-python:latest

RUN apt-get install -y wget pm-utils libusb-1.0-0

RUN mkdir -p /opt/augment00

RUN wget http://download.tinkerforge.com/tools/brickd/linux/brickd_linux_latest_armhf.deb
RUN sudo dpkg -i brickd_linux_latest_armhf.deb

EXPOSE 4223

CMD /usr/bin/brickd

