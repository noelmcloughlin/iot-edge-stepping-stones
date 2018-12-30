#!/usr/bin/env python

import sys, os
sys.path.append('../lib')
import osutils as utils

try:
    from wia import Wia
except:
    utils.install_pip('wia')
    from wia import Wia

try:
    from sense_hat import SenseHat
except:
    utils.install_pkg('sense-hat')
    from sense_hat import SenseHat

def install():
    utils.install_pip('wia')
    if not utils.is_executable('npm'):
        utils.install_nodejs('6')
    #utils.install_pkg('opencv-python')

def temperature(sense, seconds):
    while True:
        temperature=round(sense.get_temperature(),2)
        wia.Event.publish(name="temperature", data=temperature)
        sleep(int(seconds)))

def weather(sense, seconds):
    while True:
        temperature=round(sense.get_temperature(),2)
        humidity=round(sense.get_humidity(), 2)
        pressure=round(sense.get_pressure(), 2)
        wia.Event.publish(name="temperature", data=temperature)
        wia.Event.publish(name="humidity", data=humidity)
        wia.Event.publish(name="pressure", data=pressure)
        sleep(int(seconds)))

def usage():
    print("\n%s Usage:" % os.path.basename(__file__))
    print("\n\t-a --action install)
    print("\n\t-s --sense [ temp | weather ]")
    print("\n")
    sys.exit(2)

def main(argv):
    """ main """
    try:
        opts, args = getopt.getopt(argv,"a:s:",["action=","sense="])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    sense = SenseHat()
    sense.clear()
    wia = Wia()
    wia.access_token = os.environ['MY_WIA_TOKEN']

    for opt, arg in opts:
        if opt in ("-a", "--action"):
            if arg == 'install':
                install()
            else:
                usage()
        elif opt in ("-s", "--sense"):
            if arg == 'temp':
                temperature(sense, 30)
            elif arg == 'weather':
                weather(sense, 30)
            else:
                usage()
        else:
            usage()

if __name__ == "__main__":
   main(sys.argv[1:])
