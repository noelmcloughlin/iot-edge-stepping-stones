#!/usr/bin/env python

import os, sys, shutil
from subprocess import call

import sys
sys.path.append('../lib')
import osutils as utils

appname = "ble-led-matrix-gatt-server"
appdest = "/usr/local/"

def deploy:
    shutil.copy(utils.workdir + "smartlight-gatt-server", appdest + appname + "/gatt-server")
    call(['sudo', utils.workdir + '../restart_ble.py'])

deploy()
