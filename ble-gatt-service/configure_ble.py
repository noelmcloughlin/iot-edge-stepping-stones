#!/usr/bin/env python

import os, sys, shutil
from subprocess import Popen, PIPE, call

sys.path.append('../lib')
import osutils as utils

def prereqs():
    call(['sudo', 'usermod', '-G', 'staff', 'pi'])
    utils.install_pkg(['libglib2.0-dev', 'libudev-dev', 'libical-dev', 'libreadline-dev'])
    utils.install_pkg(['libdbus-1-dev', 'python-dbus', 'git'])
    utils.install_pip(['gitpython',])
        
def check_bluez_version():
    try:
        p = Popen(['bluetoothctl', '-v'], stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        output = output.split()[1]
    except:
        output = "1.0"
    return str(output)

def make_install_bluez_and_reboot(version):
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

###main###
wanted_version='5.50'
if check_bluez_version() != wanted_version:
    prereqs()
    make_install_bluez_and_reboot(wanted_version)
else:
    print("\nbluez version %s already installed" % wanted_version)

exit(0)
