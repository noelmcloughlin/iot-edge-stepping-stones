#!/usr/bin/env python

from subprocess import call
import sys
sys.path.append('../lib')
import osutils as utils

if not utils.is_executable('npm'):
    utils.install_nodejs('6')   ## version six works for Blynk anyway
utils.install_pkg('build-essential', 'npm')
