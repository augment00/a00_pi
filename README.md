# Augment00 Raspberry Pi

Augment00 uses Raspberry Pis as its principle processors in clients.

These Pis have a standard base image with will be made available for download.

Configuration is a two stage process, firstly wifi credentials uuid and credentials are provided on a usb then additional configuration is downloaded from the augment00.org server.

Applications are all run via docker compose and so can be updated remotely.

## To prepare a new micro sd card

### 1 Download Jessie Lite:

[https://www.raspberrypi.org/downloads/raspbian/] (https://www.raspberrypi.org/downloads/raspbian/)

The current build is using 2017-04-10-raspbian-jessie-lite which is also here https://www.dropbox.com/s/cfp57fjyf4cfia5/2017-04-10-raspbian-jessie-lite.zip?dl=0

### 2 Burn to card

Use Etcher [https://etcher.io/] (https://etcher.io/) to write this image to your sd card

### 3 Connect to your Pi

- Connect screen, mouse and keyboard to Pi.
- Put the sd card in the pi and boot up.
- Login with username pi and password raspberry
- type `sudo su` to become root
- type `wpa_passphrase "<wifi ssid>" "<wifi password>" >> /etc/wpa_supplicant/wpa_supplicant.conf` to set up wifi
- type `wpa_cli reconfigure` to force wfi to reset
- type `raspi-config` and then select Interfacing Options > SSH > Yes to turn on the ssh server
- type `reboot`

You can now connect to the Pi with ssh pi@raspberrypi.local if you are on the same network

### 4 Prepare the card

Then on your own computer you can use the commands in fabric.py to prepare the card. Using a command line:

- install fabric `pip install fabric`
- prepare the card `fab prepare_card`

This will take a minute or two as it will install docker and docker compose. Once complete this card is read to use.
In practice we will create an image of this card to be used in all the RPs that will be made avilable for download.

## Building Docker Images

Augment00 will use docker to manage applications. The Linux core on the Raspberry Pi is built to take advantage of its built in floating point unit.
This means that it is best to build images on a pi.

The fabric.py file has two build commands:

- `fab build_base` will build the paulharter/augment00-bootstrap-base image
- `fab build_bootstrap` will build the paulharter/augment00-bootstrap image

These commands will also push the built images to dockerhub if you first login with `fab docker_login:<password>`




