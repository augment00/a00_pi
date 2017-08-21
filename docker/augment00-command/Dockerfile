FROM augment00/augment00-python:latest

RUN mkdir -p /opt/augment00

RUN cd /opt/augment00 && git clone https://github.com/augment00/a00_command.git

RUN pip install -r /opt/augment00/a00_command/requirements.txt

WORKDIR /opt/augment00

CMD ["python", "-u", "a00_command/main.py"]

