
from subprocess import call
import os
import distutils.spawn
distutils.spawn.find_executable("notepad.exe")

workdir = str(os.getcwd()) + "/"

def is_executable(package):
    if distutils.spawn.find_executable(package):
        return True
    return False
        
def install_pip(package):
    if isinstance(package, basestring):
        package = [package,]
    try:
        for pkg in package.split():
            call(['pip', 'install', pkg])
    except:
        print("\nCannot install %s" % ''.join(package))

def install_pkg(package, os_family='debian'):
    if isinstance(package, basestring):
        package = [package,]
    try:
        for pkg in package:
            if os_family == 'debian':
                call(['sudo', 'apt-get', 'install', '-y', pkg])
    except:
        print("\nCannot install %s" % ''.join(package))

def install_nodejs(version='11'):
    url = "https://deb.nodesource.com/setup_%s.x" % version
    try:
        call(['wget', '-L', url])
        call(['sudo', '-E', 'bash', os.path.basename(url)])
    except:
        print("\nThe script %s failed" % os.path.basename(url))
    print("\nhere")
    install_pkg('nodejs')
