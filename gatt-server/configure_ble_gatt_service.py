#!/usr/bin/env python

import os, sys, shutil
from subprocess import Popen, PIPE, call
from git import Repo

sys.path.append('../lib')
import osutils as utils

def prereqs()
    call(['sudo', 'usermod', '-G', 'staff', 'pi'])
    utils.install_pkg(['libglib2.0-dev', 'libudev-dev', 'libical-dev', 'libreadline-dev'])
    utils.install_pkg(['libdbus-1-dev', 'python-dbus', 'git'])
    utils.install_pip(['gitpython',])
        
def check_bluez_version(version):
    try:
        p = Popen(['bluetoothctl', '-v'], stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        output = output.split()[1]
    except:
        output = "1.0"
    return str(output)

make_install_bluez_and_reboot(version):
    print("\nInstall BlueZ %s" % wanted_version)
    call(["sudo", "apt-get", "update"])
    call("rm -fr  bluez-*", shell=True)

    print("\nDownload BlueZ %s" % wanted_version)
    call(["wget", "www.kernel.org/pub/linux/bluetooth/bluez-" + wanted_version + ".tar.xz"])
    call(["tar", "xvf", "bluez-" + wanted_version + ".tar.xz"])

    print("\nMake BlueZ %s" % wanted_version)
    os.chdir( utils.workdir + "/bluez-" + wanted_version )
    call(["./configure", "--prefix=/usr", "--mandir=/usr/share/man", "--sysconfdir=/etc", "--localstatedir=/var", "--enable-experimental"])
    call(["make", "-j4"])

    print("\nInstall BlueZ %s binaries" % wanted_version)
    call(["sudo", "make", "install"])
    print("\n\nDone - rebooting")
    call(["sudo", "reboot"])

def service_running()
    appdesc = "BLE LED Matrix Gatt Server"
    appname = "ble-led-matrix-gatt-server"
    appdest = "/usr/local/"
    svcfile = "ble-led-gatt.service"

    print("\nSetup %s" % appdesc)
    try:
        shutil.rmtree(appdest + appname, True)
        shutil.rmtree(utils.workdir + appname, True)
    except:
        True

    Repo.clone_from("https://github.com/fxwalsh/Bluetooth-Low-Energy-LED-Matrix.git", appname)
    shutil.move(utils.workdir + appname, appdest)

    call(['sudo', 'cp', "systemd/" + svcfile, '/lib/systemd/system/'])
    try:
        call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
        call(['sudo', 'hciconfig', 'hci0', 'leadv', '0'])
    except:
        print("\nFailed to start BLE Advertising")
        exit(1)

    try:
        call(['sudo', 'systemctl', 'daemon-reload'])
        call(['sudo', 'systemctl', 'enable', svcfile])
        call(['sudo', 'systemctl', 'start', svcfile])
    except:
        call(['sudo', 'systemctl', 'start', svcfile])
        print("\nFailed to start %s" % svcfile)
        exit(1)

### main ####

#install/reboot
wanted_version='5.50'
if check_bluez_version() != wanted_version:
    prereqs()
    make_install_bluez_and_reboot()

#start service
service_running()
exit(0)

