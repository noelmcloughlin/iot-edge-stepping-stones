#!/usr/bin/env bash

sudo systemctl restart bluetooth
sudo hciconfig hci0 down
sudo hciconfig hci0 up
sudo hciconfig hci0 leadv 0
sudo systemctl restart ble-led-gatt.service 2>/dev/null
