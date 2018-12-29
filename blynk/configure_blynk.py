#!/usr/bin/env python

from subprocess import call
import os, sys, getopt
sys.path.append('../lib')
import osutils as utils

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"d:",["device=",])
    except getopt.GetoptError:
        opts = None

    if not opts:
        print("\nUsage:\n%s -d <subdir>\n" % os.path.basename(__file__))
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-d", "--device"):
            dir = arg
        else:
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()

    call(['sudo', 'apt-get', 'purge', 'node', 'nodejs', 'node.js', '-y'])
    call(['sudo', 'apt-get', 'autoremove', '-y'])
    utils.install_nodejs('6')   ## version six works for Blynk anyway
    utils.install_pkg(['build-essential', 'npm'])
    os.chdir(utils.workdir + "/" + dir)
    call(['npm', 'install', 'blynk-library', '--save', '--unsafe-perm'])

    try:
        call(['npm', 'install', 'blynk-library', '--save', '--unsafe-perm'])
        call(['npm', 'install', 'onoff', '--save', '--unsafe-perm'])
        call(['npm', 'install', 'node-sense-hat', '--save', '--unsafe-perm'])
        os.chdir(utils.workdir)
    except:
        print("\nFailed to install node packages")
        exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])
