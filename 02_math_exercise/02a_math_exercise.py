# Simple math exercise
from microbit import *
import random

while True:
    if button_a.was_pressed():
        a = random.randint(1 , 5)
        b = random.randint(1 , 5)
        op = random.randint(1 , 2)
        if op == 1:
            ops = '+'
        elif op == 2:
            ops = '*'
        if ops == '+':
            res = a+b
        elif ops == '*':
            res = a*b
        display.scroll(str(a) + ops + str(b) + '=?')
        sleep(2000)
        counter = 0
        while not (button_a.was_pressed()):
            sleep(1000)
            counter = counter + button_b.get_presses()
            if counter < 10:
                display.show(str(counter))
            else:
                display.scroll(str(counter))
        if counter == res:
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)


