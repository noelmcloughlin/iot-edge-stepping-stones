#!/usr/bin/env python

from subprocess import call
call(['pip', 'install', 'wia'])
call(['pip', 'install', 'opencv-python'])

import cv2
from wia import Wia
import os
import time

input('Hit any key to take a pic...')
vc = cv2.VideoCapture(0)
wia = Wia()
wia.access_token = os.environ['MY_WIA_TOKEN']
file_name='wia-pic.jpg'

if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
        cv2.imwrite(file_name,frame) # writes image test.bmp to disk
        dir_path = os.path.dirname(os.path.realpath(__file__))
        result = wia.Event.publish(name='photo', file=open(dir_path + '/' + file_name, 'rb'))
else:
        rval = False
