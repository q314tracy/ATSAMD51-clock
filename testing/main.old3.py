import board
import digitalio
import time
import random

#switch
switch = digitalio.DigitalInOut(board.D7)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

def rando(sw:digitalio.DigitalInOut):
    if sw.value == True:
        number = random.randint(0, 9)
        print(number)
        

while True:
    rando(switch)