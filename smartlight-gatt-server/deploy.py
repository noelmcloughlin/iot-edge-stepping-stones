#!/usr/bin/env python

import os, sys, shutil
from subprocess import call

appname = "ble-led-matrix-gatt-server"
appdest = "/usr/local/"

def deploy:
    workdir = str(os.getcwd()) + "/"
    shutil.copy(workdir + "smartlight-gatt-server", appdest + appname + "/gatt-server")
    call(['sudo', workdir + '../restart_ble.py'])

deploy
