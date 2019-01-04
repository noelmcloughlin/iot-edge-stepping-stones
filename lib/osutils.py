
from subprocess import call
import os, shutil
import distutils.spawn

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

def setup_pylib(appname, url, pydirname=None, subdir=None):
    """ Install something from git """

    try:
        from git import Repo
    except:
        utils.install_pkg('git')
        from git import Repo

    shutil.rmtree(str(pydirname))
    Repo.clone_from(url, pydirname)
    if appname:
        os.chdir(str(pydirname))
        if subdir:
            os.chdir(str(subdir))
        call(['sudo', 'python', './setup.py', 'install'])
        os.chdir(workdir)

def install_lib(libpackage):
    """ Install and/or import python library or function """

    if libpackage == 'sense-hat':
        install_pkg('sense-hat')

    elif libpackage == 'bme680-python':
        url = 'https://github.com/pimoroni/bme680-python.git'
        setup_pylib(workdir + '/bme680-python', url, 'bme680-python', 'library')

    else:
        print("\n unsupported library %s" % libpackage)
        exit(1)
