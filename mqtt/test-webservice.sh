#!/usr/bin/env bash

./configure_mqtt.py 
FLASK_APP=hello.py
python temp_db_data.py 
sudo ./sense_api.py 
