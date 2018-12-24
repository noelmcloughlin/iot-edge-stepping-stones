#!/usr/bin/env python

from subprocess import call

def package_install():
    #Python modules
    pkgs = "wia"
    cmd = "pip "
    add = "install "
    for items in pkgs.split():
        command = str(cmd) + str(add) + str(items)
        call(command.split())
        command = "sudo " + str(cmd) + str(add) + str(items)
        call(command.split())

package_install()
