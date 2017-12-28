FROM augment00/augment00-command:0.0.2

RUN mkdir -p /var/opt/augment00/recordings
RUN mkdir -p /var/opt/augment00/dev/recordings
ADD test_mov.mov /var/opt/augment00/dev/recordings/test_mov.mov

# redoing the source code
RUN rm -rf /opt/augment00/a00_command
RUN cd /opt/augment00 && git clone https://github.com/augment00/a00_command.git