
import random
import auth

import os
import json
import shutil
import subprocess


import requests

ALPHA_NUMERIC = "abcdefghijklmnopqrstuvwxyz0123456789"

MOUNT_DIR = "/mnt/usb"
USB_CONFIG_FOLDER = os.path.join(MOUNT_DIR, "augment00")
AUGMENT00_CREDS_PREFIX = "augment00_creds"
INSTALLED_CREDS_PATH = "/etc/opt/augment00/augment00_creds.json"
CONFIG_DIR = "/etc/opt/augment00"

CONFIG_OWNER = "pi"
DOCKER_COMPOSE_FILEPATH = os.path.join(CONFIG_DIR, "docker-compose.yml")


def mount_usb():
    if not os.path.exists(MOUNT_DIR):
        os.makedirs(MOUNT_DIR)
    cmd = "mount /dev/sda1 /mnt/usb"
    subprocess.call(cmd, shell=True)

def generateNewRandomAlphaNumeric(length):
    random.seed()
    values = []
    for i in range(length):
        values.append(random.choice(ALPHA_NUMERIC))
    return "".join(values)


def get_serial():
  # Extract serial from cpuinfo file
  cpu_serial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
          cpu_serial = line[10:26]
    f.close()
  except:
      cpu_serial = "ERROR000000000"

  return cpu_serial




def update_config():

    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    creds_path = None

    for filename in os.listdir(USB_CONFIG_FOLDER):
        if filename.startswith(AUGMENT00_CREDS_PREFIX):
            creds_path = os.path.join(USB_CONFIG_FOLDER, filename)

    if creds_path is None:
        return

    with open(creds_path, "r") as f:
        creds = json.loads(f.read())

    config = auth.get_config(creds, get_serial())

    if config is not None:
        write_config_files(config["config"], CONFIG_DIR, CONFIG_OWNER, 0755)
        # shutil.copy(creds_path, INSTALLED_CREDS_PATH)


def write_config_files(config, base_dir, owner, mode):

    for config_file in config:
        path = config_file["path"]
        path = path[1:] if path.startswith("/") else path
        dst_file_path = os.path.join(base_dir, path)
        dir = os.path.dirname(dst_file_path)
        if not os.path.exists(dir):
            os.makedirs(dir)
        if os.path.exists(dst_file_path):
            os.remove(dst_file_path)
        with open(dst_file_path, "w") as f:
            f.write(config_file["text"])
        os.chmod(dst_file_path, mode)
        # uid = getpwnam(owner).pw_uid
        # gid = getpwnam(owner).pw_gid
        # os.chown(dst_file_path, uid, gid)




if __name__ == '__main__':
    print "running augment00 bootstrap"
    mount_usb()
    update_config()