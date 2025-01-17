import board
import time
import random
import asyncio
from digitalio import DigitalInOut

#pins
segment_pins = [
    board.D10, #a
    board.D9, #b
    board.D1, #c
    board.D0, #d
    board.D5, #e
    board.D11, #f
    board.D12, #g
    board.D7, #decimal
]
digit_pins = [
    board.D4, #digit 1
    board.D3, #digit 2
    board.A5, #digit 3
    board.A2, #digit 4
    board.A4, #digit 5
    board.A3 # digit 6
]  

#take list of pins and declare type
segments = [DigitalInOut(pin) for pin in segment_pins]
digits = [DigitalInOut(pin) for pin in digit_pins]

#set pins to outputs by default and write normal states of outputs
for led in segments:
    led.switch_to_output(True)
for pin in digits:
    pin.switch_to_output(False)

#mapping for numbers on display, based off truth table for display
#in order a, b, c, d, e, f, g, dec
number_mapping = {
    0: [True, True, True, True, True, True, False, False],
    1: [False, True, True, False, False, False, False, False],
    2: [True, True, False, True, True, False, True, False],
    3: [True, True, True, True, False, False, True, False],
    4: [False, True, True, False, False, True, True, False],
    5: [True, False, True, True, False, True, True, False],
    6: [True, False, True, True, True, True, True, False],
    7: [True, True, True, False, False, False, False, False],
    8: [True, True, True, True, True, True, True, False],
    9: [True, True, True, True, False, True, True, False]
}

#set led state
def set_led(led_indexed:DigitalInOut, state:bool):
    if state == True:
        led_indexed.value = False
    elif state == False:
        led_indexed.value = True

#set digit state
def set_digit(digit_indexed:DigitalInOut, state:bool):
    if state == True:
        digit_indexed.value = True
    elif state == False:
        digit_indexed.value = False

#clear all led states to off
def clear_all(led_list:DigitalInOut, digit_list:DigitalInOut):
    for led in led_list:
        set_led(led, False)
    for digit in digit_list:
        set_digit(digit, False)

#set number on specified digit
def set_number(led_list:DigitalInOut, digit_list:DigitalInOut, digit_index:int, num:int):
    set_digit(digit_list[digit_index], True)
    counter = 0
    for led in led_list:
        set_led(led, number_mapping[num][counter])
        counter += 1
    clear_all(led_list, digit_list)

#set display to passed integer
def set_display(led_list:DigitalInOut, digit_list:DigitalInOut, num):
    num_padded = f"{num:06}"
    counter = 0
    for num in digit_list:
        set_number(led_list, digit_list, counter, int(num_padded[counter]))
        counter += 1

#get init time
time_init_seconds = time.time()

#main loop
while True:
    time_seconds = time.time() - time_init_seconds
    set_display(segments, digits, time_seconds)