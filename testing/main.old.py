# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Digital In Out example"""
import time
import board
from digitalio import DigitalInOut, Direction

#led interface for heartbeat
led_status = DigitalInOut(board.D7)
led_status.direction = Direction.OUTPUT

#heartbeat function 
def heartbeat(led):
    if led.value == False:
        led.value = True
        time.sleep(1)
        led.value = False
    time.sleep(1)



#main loop
while True:
    heartbeat(led_status)



