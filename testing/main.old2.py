import board
import pwmio
import time
from digitalio import DigitalInOut, Direction, Pull

peizo_speaker = pwmio.PWMOut(board.LED, frequency=5000)

time_step = 0.1
duty_step = 10
duty_max = 1000
duty_min = 0

def heartbeat(max:int, min:int, step:int, debounce:float):
    for duty in range(min, max, step):
        peizo_speaker.duty_cycle = duty
        time.sleep(debounce)
        print(duty)
    for duty in range(max, min, -step):
        peizo_speaker.duty_cycle = duty
        time.sleep(debounce)
        print(duty)

while True:
    heartbeat(duty_max, duty_min, duty_step, time_step)