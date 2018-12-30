#!/usr/bin/env python
#####################################
# Sense temperature from SenseHat
# Send data to third party api.
#####################################

from subprocess import call
import os, sys, json, time, urllib2, getopt

sys.path.append('../lib')
import osutils as utils

try:
    from sense_hat import SenseHat
except:
    utils.install_pkg('sense-hat')
    from sense_hat import SenseHat

def writeData(url, temp):
    """ Sending data to url """
    conn = urllib2.urlopen(url + '&field1=%s' % (temp))
    print(conn.read)
    conn.close()

def temperature(sense, url, seconds):
    """ Get temperature from SenseHat """
    temp=round(sense.get_temperature(), 2)
    writeData(url, temp)
    sense.show_message(str(temp))
    time.sleep(seconds)

def usage():
    """ Usage """
    print("\nUsage: %s" % os.path.basename(__file__))
    print("\n\t-s --sense temp")
    print("\n\t-t --tell thingspeak")
    print("\n")
    sys.exit(2)
    
def main(argv):
    """ main """
    try:
        opts, args = getopt.getopt(argv,"s:t:",["sense=", "tell="])
    except getopt.GetoptError:
        usage()

    if not opts:
        usage()

    for opt, arg in opts:
        if opt in ("-s", "--sense"):
            sense = SenseHat()
            sensor=arg
        elif opt in ("-t", "--type"):
            if arg == 'thingspeak':
                uri='https://api.thingspeak.com'
                url= uri + '/update?api_key=%s' % os.environ['MY_THINGSPEAK_WTOKEN']
            else:
                usage()
        else:
            usage()

    if sense and sensor:
        while True:
            if str(sensor) == "temp":
                temperature(sense, url, 60)
            else:
                usage()
    else:
        usage()


if __name__ == "__main__":
   main(sys.argv[1:])
exit(0)
