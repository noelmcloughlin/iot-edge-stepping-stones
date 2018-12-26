# iot-ble-gatt-server
Adding Bluetooth Low Energy LED Matrix Gatt Server service for IoT

Rasbian on Raspberry Pi 3 B+

* Clone this repo

* Execute command to setup Bluetooth 5.50 prerequisites (system reboot)

.. code-block:: bash

        ./configure_ble_gatt_service.py

* Execute command to setup BLE GATT Service

.. code-block:: bash

        ./configure_ble_gatt_service.py

* Start the service

.. code-block:: bash

        sudo systemctl start ble-led-gatt.service

* Your PI is now BLE advertising and waiting for a device connections.




