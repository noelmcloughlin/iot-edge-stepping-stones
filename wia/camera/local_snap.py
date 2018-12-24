#!/usr/bin/env python3

from wia import Wia
import time
from picamera import PiCamera

wia = Wia()
## INSERT YOUR SECRET KET
wia.access_token = os.environ['MY_WIA_TOKEN']
camera = PiCamera()

## Halt execution until
input('Look at the camera and hit "Enter" to take a pic...')

## Start up PiCam
camera.start_preview()
## sleep for a few seconds to let camera focus/adjust to light
time.sleep(5)
## Capture photo
camera.capture('/home/pi/image.jpg')
## Stop the PiCam
camera.stop_preview()

## Publish "photo" event to Wia. Include the photo file. 
result = wia.Event.publish(name='photo', file=open('/home/pi/image.jpg', 'rb'))
