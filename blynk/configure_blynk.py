#!/usr/bin/env python

from subprocess import call
import sys
sys.path.append('../lib')
import osutils as utils

if not utils.is_executable('npm'):
    utils.install_nodejs('6')   ## version six works for Blynk anyway
utils.install_pkg('build-essential', 'npm')

try:
    call(['sudo', 'npm', 'install', 'blynk-library', '--save'])
    call(['sudo', 'npm', 'install', 'onoff', '--save'])
except:
    print("\nFailed to install node packages")
    exit(1)
