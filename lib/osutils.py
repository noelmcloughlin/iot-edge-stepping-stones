
from subprocess import call
import os

workdir = str(os.getcwd()) + "/"

def is_executable(package):
    return call([package, "-v"])
        
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
        for pkg in package.split():
            if os_family == 'debian':
                call(['sudo', 'apt-get', 'install', '-y', package])
    except:
        print("\nCannot install %s" % ''.join(package))

def install_nodejs(version='11', os_family='debian'):
    if os_family == 'debian':
        url = "https://deb.nodesource.com/setup_%s.x" % version
        try:
            call(['wget', '-L', url])
            call(['sudo', '-E', 'bash', os.path.basename(url)])
            install_pkg('nodejs')
        except:
            print("\nCannot install nodejs %s" % version)
