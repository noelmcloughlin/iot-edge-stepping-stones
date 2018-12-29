#!/usr/bin/env python

from subprocess import call
import os, sys, getopt
sys.path.append('../lib')
import osutils as utils

def main(argv):
    try:
        call(['sudo', 'apt-get', 'purge', 'node', 'nodejs', 'node.js', '-y'])
        call(['sudo', 'apt-get', 'autoremove', '-y'])
        utils.install_nodejs('6')   ## version six works for Blynk anyway
        utils.install_pkg(['build-essential', 'npm'])
    except:
        print("\nFailed to configure packages")
        exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])
