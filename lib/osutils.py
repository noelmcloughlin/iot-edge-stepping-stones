
from subprocess import call
import os
import distutils.spawn
distutils.spawn.find_executable("notepad.exe")

workdir = str(os.getcwd()) + "/"

def is_executable(package):
    if distutils.spawn.find_executable(package):
        return True
    return False
        
def install_npm_lib(package): 
    if isinstance(package, basestring):
        package = [package,]
    try:
        for pkg in package.split():
            call(['npm', 'install', pkg, '--save', '--unsafe-perm'])
    except:
        print("\nCannot install %s" % ''.join(package))

def install_pip(package):
    if isinstance(package, basestring):
        package = [package]
    try:
        for pkg in package:
            call(['pip', 'install', pkg])
    except:
        print("\nCannot install %s" % ''.join(package))

def install_pkg(package):
    if isinstance(package, basestring):
        package = [package,]
    try:
        for pkg in package:
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
    install_pkg('nodejs')

def import_lib(name, func=None):
    """ Import a python library or function """
    try:
        if func:
            exec('from %s import %s' % (name, func))
        else:
            exec('import %s' % name)
        return True
    except:
        return False

def install_lib(name, func=None):
    """ Install and/or import python library or function """
    result = False
    try:
        result = import_pylib(name, func)
    except:
        if name == 'sense-hat':
            install_pkg('sense-hat')
        elif name == 'bme680':
            install_bme680()
        else:
            print("\n unsupported library %s" % name)
            exit(1)
