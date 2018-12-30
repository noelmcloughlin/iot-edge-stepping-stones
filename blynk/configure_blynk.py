#!/usr/bin/env python
#####################################
# Install or reinstall nodejs.
# Install node libraries into appdir.
#####################################

from subprocess import call
import os, sys, getopt

sys.path.append('../lib')
import osutils as utils

def package_failure():
    print("\nFailed to configure packages")
    exit(1)

def install_node():
    try:
        utils.install_nodejs('6')   ## version six works for Blynk anyway
        utils.install_pkg(['build-essential', 'npm'])
    except:
        package_failure()

def reinstall_node():
    try:
        call(['sudo', 'apt-get', 'purge', 'node', 'nodejs', 'node.js', '-y'])
        call(['sudo', 'apt-get', 'autoremove', '-y'])
    except:
        package_failure()
    install_node()

def install_node_libs(dir):
    try:
        os.chdir(dir)
        utils.install_npm_lib('blynk-library', 'onoff', 'node-sense-hat', 'wia',])
        os.chdir(utils.workdir)
    except:
        package_failure()

def usage():
    print("\n%s Usage:" % os.path.basename(__file__))
    print("\n\t-d --device <device_nodejs_subdir>")
    print("\n\t-n --node [ install|reinstall ] NodeJS")
    print("\n")
    sys.exit(2)
    
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"d:n:",["device=","node="])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    for opt, arg in opts:
        if opt in ("-d", "--device"):
            if arg:
                install_node_libs(workdir + '/' + arg):
            else:
                usage:
        elif opt in ("-n", "--node"):
            if arg == 'install':
                install_node()
            elif arg == 'reinstall':
                reinstall_node()
            else:
                usage()
        else:
            usage()

if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
