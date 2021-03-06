# GrovePi + Grove MOSFET
# http://www.seeedstudio.com/wiki/Grove_-_MOSFET

import time
import grovepi

# MOSFET is also a kind of switch, but its switching frequency can reach up to 5MHz, much faster than normal mechanical relay.
# There are two screw terminals on opposite sides of the board.
# One side for power source and the other side for the device you want to control.

# Connect the Grove MOSFET to analog port A0
# SIG,NC,VCC,GND
mosfet = 0

grovepi.pinMode(mosfet,"OUTPUT")
time.sleep(1)

while True:
    try:
        # Full speed
        grovepi.analogWrite(mosfet,255)
        print "full speed"
        time.sleep(2)

        # Half speed
        grovepi.analogWrite(mosfet,128)
        print "half speed"
        time.sleep(2)

        # Off
        grovepi.analogWrite(mosfet,0)
        print "off"
        time.sleep(2)

    except KeyboardInterrupt:
        grovepi.analogWrite(mosfet,0)
        break
    except IOError:
        print "Error"