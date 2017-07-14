FROM augment00/augment00-python:latest

RUN mkdir -p /opt/augment00
ADD augment00-bootstrap /opt/augment00/augment00-bootstrap

WORKDIR /opt/augment00

CMD ["python", "augment00-bootstrap/main.py"]





