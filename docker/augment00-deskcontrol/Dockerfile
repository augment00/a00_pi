FROM augment00/augment00-python:latest

RUN mkdir -p /opt/augment00

RUN cd /opt/augment00 && git clone https://github.com/arupiot/deskcontrol.git

RUN git pull origin master

RUN pip install -r /opt/augment00/deskcontrol/requirements.txt

WORKDIR /opt/augment00

CMD ["python", "deskcontrol/controller.py"]

