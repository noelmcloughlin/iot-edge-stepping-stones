
import sys
sys.path.append('..')
sys.path.append('../lib')
import osutils as utils

utils.install_pkg(['mosquitto', 'mosquitto-client',])
utils.install_pip(['paho-mqtt', 'tinyDB', 'flask', 'flask-cors',])
