#!/usr/bin/env python

### https://developers.wia.io/docs/raspberry-pi-3-model-b-plus:

import os
from wia import Wia
wia = Wia()
wia.access_token = os.environ['MY_WIA_TOKEN']
wia.Event.publish(name="hello-wia", data="")
