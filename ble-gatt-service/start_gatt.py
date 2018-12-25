#!/usr/bin/env python

import sys, shutil
from subprocess import Popen, PIPE, call
sys.path.append('../lib')
import osutils as utils

def ble_advertising():
    try:
        from git import Repo
    except:
        utils.install_pkg('git')
        from git import Repo

    appdesc = "BLE LED Matrix Gatt Server"
    appname = "ble-led-matrix-gatt-server"
    appdest = "/usr/local/"
    svcfile = "ble-led-gatt.service"

    print("\nSetup %s" % appdesc)
    try:
        shutil.rmtree(appdest + appname)
        shutil.rmtree(utils.workdir + appname)
    except:
        print("\nFailed (hint: try sudo)")
        exit(1)

    Repo.clone_from("https://github.com/fxwalsh/Bluetooth-Low-Energy-LED-Matrix.git", appname)
    shutil.move(utils.workdir + appname, appdest)

    call(['sudo', 'cp', "systemd/" + svcfile, '/lib/systemd/system/'])
    try:
        call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
        call(['sudo', 'hciconfig', 'hci0', 'leadv', '0'])
    except:
        print("\nFailed to start BLE Advertising")
        exit(1)

def gatt_service_started():
    try:
        call(['sudo', 'systemctl', 'daemon-reload'])
        call(['sudo', 'systemctl', 'enable', svcfile])
        call(['sudo', 'systemctl', 'start', svcfile])
    except:
        call(['sudo', 'systemctl', 'start', svcfile])
        print("\nFailed to start %s" % svcfile)
        exit(1)

### main ####
ble_advertising()
gatt_service_started()
exit(0)
