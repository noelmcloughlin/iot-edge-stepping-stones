#!/usr/bin/env python

import sys
sys.path.append('../lib')
import osutils as utils

utils.install_pip('wia')
if not utils.is_executable('npm'):
    utils.install_nodejs('6')
#utils.install_pkg('opencv-python')
