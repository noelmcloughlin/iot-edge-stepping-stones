#!/usr/bin/env python

import os, sys, shutil
from subprocess import Popen, PIPE, call

def package_install():
    #Linux packages
    pkgs = "mosquitto sense-hat mosquitto-clients"
    cmd = "sudo apt "
    add = "install -y "
    for item in pkgs.split():
        command = str(cmd) + str(add) + str(item)
        call(command.split())

    #Python modules
    pkgs = "paho-mqtt tinyDB flask flask-cors"
    cmd = "pip "
    add = "install "
    for items in pkgs.split():
        command = str(cmd) + str(add) + str(items)
        call(command.split())
        command = "sudo " + str(cmd) + str(add) + str(items)
        call(command.split())

def mosquitto_repo():
    ### Unused on Raspbian
    call(["wget", "http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key"])
    call(["sudo", "apt-key", "add", "mosquitto-repo.gpg.key"])
    if os.path.isfile("mosquitto-repo.gpg.key"):
        os.remove("mosquitto-repo.gpg.key")

package_install()
