#!/usr/bin/env python

import os, sys
from subprocess import call

def restart_bluez_ble_app():
    call(['sudo', 'systemctl', 'restart', 'bluetooth'])
    call(['sudo', 'hciconfig', 'hci0', 'down'])
    call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
    call(['sudo', 'hciconfig', 'hci0', 'up'])
    call(['sudo', 'hciconfig', 'hci0', 'name', 'RPi'])
    call(['sudo', 'hciconfig', 'hci0', 'leadv', '0'])
    #call(['sudo', 'systemctl', 'restart', 'ble-led-gatt'])

restart_bluez_ble_app
