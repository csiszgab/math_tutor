# Write your code here :-)
from microbit import *
steps = 0

while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.scroll(steps)
