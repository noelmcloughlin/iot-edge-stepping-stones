
from subprocess import call
import os

def is_executable(package):
    return call([package, "-v"])
        
def install_pip(package):
    try:
        call(['pip', 'install', package])
    except:
        print("\nCannot find %s to install" % package)

def install_pkg(package, os_family='debian'):
    if os_family == 'debian':
        try:
            call(['sudo', 'apt-get', 'install', '-y', package])
        except:
            print("\nCannot find %s to install" % package)

def install_nodejs(os_family='debian'):
    version = "11"
    if os_family == 'debian':
        url = "https://deb.nodesource.com/setup_%s.x" % version
        try:
            call(['wget', '-L', url])
            call(['sudo', '-E', 'bash', os.path.basename(url)])
            install_pkg('nodejs')
        except:
            print("\nCannot install nodejs")
