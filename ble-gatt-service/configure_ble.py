#!/usr/bin/env python
##################################
## Install or Restart BLE
##################################

import os, sys, shutil, getopt
from subprocess import Popen, PIPE, call

sys.path.append('../lib')
import osutils as utils

def device_libs():
    call(['sudo', 'usermod', '-G', 'staff', 'pi'])
    utils.install_pkg(['libglib2.0-dev', 'libudev-dev', 'libical-dev', 'libreadline-dev'])
    utils.install_pkg(['libdbus-1-dev', 'python-dbus', 'git'])
    utils.install_pip(['gitpython',])
        
def bluez_version():
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

def restart_bluez_ble():
    call(['sudo', 'systemctl', 'restart', 'bluetooth'])
    call(['sudo', 'hciconfig', 'hci0', 'down'])
    call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
    call(['sudo', 'hciconfig', 'hci0', 'up'])
    call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
    call(['sudo', 'hciconfig', 'hci0', 'leadv', '0'])
    #call(['sudo', 'systemctl', 'restart', 'ble-led-gatt'])

def install_ble():
    wanted_version='5.50'
    if bluez_version() != wanted_version:
        device_libs()
        make_install_bluez_and_reboot(wanted_version)
    else:
        print("\nbluez version %s already installed" % wanted_version)

def usage():
    print("\nUsage:\n%s -a [ install|restart ]\n" % os.path.basename(__file__))
    sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"a:",["action=",])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    for opt, arg in opts:
        if opt in ("-a", "--action"):
            if arg == 'install':
                install_ble()
            elif arg == 'restart':
                restart_bluez_ble()
            else:
                usage()
        else:
            usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
