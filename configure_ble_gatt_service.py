#!/usr/bin/env python

import os, sys, shutil
from subprocess import Popen, PIPE, call

def package_install():
    call(['sudo', 'usermod', '-G', 'staff', 'pi'])
    #Linux packages
    pkgs = "bluez git python-dbus libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev"
    cmd = "sudo apt "
    add = "install -y "
    for items in pkgs.split():
        command = str(cmd) + str(add) + str(items)
        call(command.split())

    #Python modules
    pkgs = "gitpython"
    cmd = "pip "
    add = "install "
    for items in pkgs.split():
        command = str(cmd) + str(add) + str(items)
        call(command.split())
        
## Get bluetooth version
wanted_version = "5.50"
workdir = str(os.getcwd()) + "/"
try:
    p = Popen(['bluetoothctl', '-v'], stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
except:
    output = "Bluetooth: 1.0"

if output.split()[1] != str(wanted_version):
    package_install()
    print("\nInstall BlueZ %s" % wanted_version)
    call(["sudo", "apt-get", "update"])
    call("rm -fr  bluez-*", shell=True)

    print("\nDownload BlueZ %s" % wanted_version)
    call(["wget", "www.kernel.org/pub/linux/bluetooth/bluez-" + wanted_version + ".tar.xz"])
    call(["tar", "xvf", "bluez-" + wanted_version + ".tar.xz"])

    print("\nMake BlueZ %s" % wanted_version)
    os.chdir( workdir + "/bluez-" + wanted_version )
    call(["./configure", "--prefix=/usr", "--mandir=/usr/share/man", "--sysconfdir=/etc", "--localstatedir=/var", "--enable-experimental"])
    call(["make", "-j4"])

    print("\nInstall BlueZ %s binaries" % wanted_version)
    call(["sudo", "make", "install"])
    print("\n\nNow reboot (sudo reboot)")
    call(["sudo", "reboot"])

from git import Repo

#GATT Server
appdesc = "BLE LED Matrix Gatt Server"
appname = "ble-led-matrix-gatt-server"
appdest = "/usr/local/"
svcfile = "ble-led-gatt.service"

print("\nSetup %s" % appdesc)
try:
    shutil.rmtree(appdest + appname, True)
    shutil.rmtree(workdir + appname, True)
except:
    True

Repo.clone_from("https://github.com/fxwalsh/Bluetooth-Low-Energy-LED-Matrix.git", appname)
shutil.move(workdir + appname, appdest)

call(['sudo', 'cp', "systemd/" + svcfile, '/lib/systemd/system/'])
try:
    call(['sudo', 'hciconfig', 'hci0', 'name', 'rPi3B+'])
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

exit(0)

