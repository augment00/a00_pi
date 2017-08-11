FROM augment00/augment00-python:latest

RUN mkdir -p /opt/augment00

RUN cd /opt/augment00 && git clone https://github.com/arupiot/deskcontrol.git

RUN pip install -r /opt/augment00/deskcontrol/requirements.txt
RUN pip install -e git+https://github.com/augment00/a00_command.git#egg=a00_command

ADD config_local.py /opt/augment00/deskcontrol/deskcontrol

WORKDIR /opt/augment00

CMD ["python", "-u", "deskcontrol/deskcontrol/controller.py"]

