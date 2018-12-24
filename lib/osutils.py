
from subprocess import call
import os

def install_pip(package):
    call(['pip', 'install', package])

def install_pkg(package, os_family='debian'):
    if os_family == 'debian':
        call(['sudo', 'apt-get', 'install', '-y', package])

def install_nodejs(os_family='debian'):
    version = "11"
    if os_family == 'debian':
        url = "https://deb.nodesource.com/setup_%s.x" % version
        call(['wget', '-L', url])
        call(['sudo', '-E', 'bash', os.path.basename(url)])
        install_pkg('nodejs')
