FROM augment00/augment00-python:latest

RUN pip install python-firebase

RUN mkdir -p /opt/augment00
ADD augment00_command /opt/augment00/augment00_command



WORKDIR /opt/augment00

CMD ["python", "augment00_command/main.py"]








