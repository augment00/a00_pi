from crypt import crypt
from fabric.api import local, settings, abort, run, env, sudo, put, get, prefix
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from config import PI_PASSWORD

env.hosts = ["%s:%s" % ("raspberrypi.local", 22)]
#env.hosts = ["%s:%s" % ("169.254.162.179", 22)]
env.user = "pi"
env.password = PI_PASSWORD

BOOTSTRAP_VERSION = "0.0.1"
PYTHON_VERSION = "0.0.2"
TEST_VERSION = "0.0.1"
DESKCONTROL_VERSION = "0.0.3"
BRICKD_VERSION = "0.0.1"
COMMAND_VERSION = "0.0.1"

RASPIAN_VERSION = "RASPBIAN STRETCH LITE sept 2017"


############################################################################
##              Preparing the base disc image from JESSIE_VERSION
############################################################################

"""
    before you can prepare the card you have to connect to your pi. Login and then:

    "sudo su"
    'wpa_passphrase "Container 20" "eggandchips" >> /etc/wpa_supplicant/wpa_supplicant.conf'
    "wpa_cli reconfigure"

    "raspi-config"

    Interfacing Options > SSH > Yes

    reboot
"""


def prepare_card():
    change_password()
    _change_graphics_memory()
    install_docker()
    # docker_login(password)
    _add_bootstrap()
    _reduce_logging()
    reduced_writes()
    add_resize()

    # sudo("reboot")


def change_password():
    env.password = "raspberry"
    crypted_password = crypt(PI_PASSWORD, 'salt')
    sudo('usermod --password %s %s' % (crypted_password, env.user), pty=False)


def _change_graphics_memory():
    sudo('echo "gpu_mem=16" >> /boot/config.txt')

def reduced_writes():
    """
    a set of optimisations from

    http://www.zdnet.com/article/raspberry-pi-extending-the-life-of-the-sd-card/

    and

    https://narcisocerezo.wordpress.com/2014/06/25/create-a-robust-raspberry-pi-setup-for-24x7-operation/
    """
    # minimise writes
    use_ram_partitions()
    _stop_fsck_running()
    _redirect_logrotate_state()
    _dont_update_fake_hwclock()
    _dont_do_man_indexing()
    _remove_swap()


def use_ram_partitions():
    sudo('echo "tmpfs    /tmp    tmpfs    defaults,noatime,nosuid,size=100m    0 0" >> /etc/fstab')
    sudo('echo "tmpfs    /var/tmp    tmpfs    defaults,noatime,nosuid,size=30m    0 0" >> /etc/fstab')
    sudo('echo "tmpfs    /var/log    tmpfs    defaults,noatime,nosuid,mode=0755,size=100m    0" >> /etc/fstab')


def _redirect_logrotate_state():
    sudo("rm /etc/cron.daily/logrotate")
    put("logrotate", "/etc/cron.daily/logrotate", use_sudo=True)
    sudo("chmod 755 /etc/cron.daily/logrotate")
    sudo("chown root /etc/cron.daily/logrotate")
    sudo("chgrp root /etc/cron.daily/logrotate")

def _stop_fsck_running():
    sudo("tune2fs -c -1 -i 0 /dev/mmcblk0p2")

def _dont_update_fake_hwclock():
    sudo("rm /etc/cron.hourly/fake-hwclock")

def _dont_do_man_indexing():
    sudo("rm  /etc/cron.weekly/man-db")
    sudo("rm  /etc/cron.daily/man-db")

def _remove_swap():
    sudo("update-rc.d -f dphys-swapfile remove")
    sudo("swapoff /var/swap")
    sudo("rm /var/swap")

def _reduce_logging():

    ## add our own rsyslog.conf
    sudo("rm /etc/rsyslog.conf")
    put("rsyslog.conf", "/etc/rsyslog.conf", use_sudo=True)
    sudo("chmod 755 /etc/rsyslog.conf")
    sudo("chown root /etc/rsyslog.conf")
    sudo("chgrp root /etc/rsyslog.conf")


def _add_bootstrap():

    # build_bootstrap()
    sudo("mkdir -p /opt/augment00")
    put("start.sh", "/opt/augment00/start.sh", use_sudo=True)
    sudo("chmod 755 /opt/augment00/start.sh")

    put("wifi.py", "/opt/augment00/wifi.py", use_sudo=True)
    sudo("chmod 755 /opt/augment00/wifi.py")

    ## add our own rc.local
    sudo("rm /etc/rc.local")
    put("rc.local", "/etc/rc.local", use_sudo=True)
    sudo("chmod 755 /etc/rc.local")
    sudo("chown root /etc/rc.local")
    sudo("chgrp root /etc/rc.local")


def add_resize():

    sudo('printf " quiet init=/usr/lib/raspi-config/init_resize.sh" >> /boot/cmdline.txt')
    put("resize2fs_once", "/etc/init.d/resize2fs_once", use_sudo=True)
    sudo("chmod +x /etc/init.d/resize2fs_once")
    sudo("chown root /etc/init.d/resize2fs_once")
    sudo("chgrp root /etc/init.d/resize2fs_once")
    sudo("systemctl enable resize2fs_once")


def build_bootstrap():
    tag = BOOTSTRAP_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="augment00/augment00-bootstrap:%s" '
         'docker/augment00-bootstrap' % tag)
    sudo('docker tag augment00/augment00-bootstrap:%s augment00/'
         'augment00-bootstrap:latest' % tag)
    sudo('docker push augment00/augment00-bootstrap:latest')


def install_docker():

    # install docker
    run("curl -sSL get.docker.com | sh")

    # sets up service
    run("sudo systemctl enable docker")

    # allows pi use to use docker
    run("sudo usermod -aG docker pi")

    # installs cocker compose
    sudo("curl --silent --show-error --retry 5 https://bootstrap.pypa.io/"
         "get-pip.py | sudo python2.7")
    sudo("pip install docker-compose")


############################################################################
##              Docker commands for building other images                       ##
############################################################################


def docker_login(password):
    sudo('docker login -u augment00 -p "%s"' % password)


def push_bootstrap():
    sudo('docker push augment00/augment00-bootstrap:latest')


def build_python():
    tag = PYTHON_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="augment00/augment00-python:%s" docker/augment00-python' % tag)
    sudo('docker push augment00/augment00-python:%s' % tag)
    sudo('docker tag augment00/augment00-python:%s augment00/augment00-python:latest' % tag)
    sudo('docker push augment00/augment00-python:latest')


def build_deskcontrol():
    tag = DESKCONTROL_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="augment00/augment00-deskcontrol:%s" docker/augment00-deskcontrol' % tag)
    sudo('docker push augment00/augment00-deskcontrol:%s' % tag)
    sudo('docker tag augment00/augment00-deskcontrol:%s augment00/augment00-deskcontrol:latest' % tag)
    sudo('docker push augment00/augment00-deskcontrol:latest')


def build_command():
    tag = COMMAND_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="augment00/augment00-command:%s" docker/augment00-command' % tag)
    sudo('docker push augment00/augment00-command:%s' % tag)
    sudo('docker tag augment00/augment00-command:%s augment00/augment00-command:latest' % tag)
    sudo('docker push augment00/augment00-command:latest')


def build_brickd():
    tag = BRICKD_VERSION
    put("docker", "~")
    sudo('docker build --no-cache=true -t="augment00/augment00-brickd:%s" docker/augment00-brickd' % tag)
    sudo('docker push augment00/augment00-brickd:%s' % tag)
    sudo('docker tag augment00/augment00-brickd:%s augment00/augment00-brickd:latest' % tag)
    sudo('docker push augment00/augment00-brickd:latest')


def test():
    put("test.txt", "~")

def get_file():

    get("/etc/cron.daily/logrotate")
















