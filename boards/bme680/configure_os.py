#!/usr/bin/env python

import os, sys, shutil
from subprocess import Popen, PIPE, call
sys.path.append('../../lib')
import osutils as utils

def get_software():
    try:
        from git import Repo
    except:
        utils.install_pkg('git')
        from git import Repo

    pylib="piromoni"
    dirname="bme680-python"
    print("\nInstall %s python library" % pylib)

    ## cleanup old dir
    if os.path.isdir(utils.workdir + '/' + dirname):
        try:
            shutil.rmtree(utils.workdir + '/' + dirname)
        except:
            print("\nFailed to remove %s directory" % dirname)
            exit(1)

    ##use python library from Pimoroni
    url="https://github.com/pimoroni/bme680-python.git"
    try:
        Repo.clone_from(url, dirname)
        os.chdir(workdir + '/' + dirname)
        call(['sudo', 'python', 'setup.py', 'install'])
    except:
        print("\nFailed to install %s python library" % pylib)
        exit(1)
    os.chdir(workdir)

### main ####
get_software()
exit(0)
