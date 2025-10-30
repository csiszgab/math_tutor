# Simple math exercise
from microbit import *
import random
import time
import os

no_exercises=5

while True:
    while not button_a.is_pressed():
        sleep(1000)
        exercise_level_tuple = ((1, Image.HAPPY), (2, Image.SAD), (3, Image.ANGRY))
        level = 0
        if button_a.was_pressed():
            while not button_a.was_pressed():
                display.show(exercise_level_tuple[level][1])
                if button_b.was_pressed():
                    level=(level + button_b.get_presses()) % 3
                    display.show(exercise_level_tuple[level][1])
        display.show(level)
    
    exercise_count=1
    result_list=[]
    result_string=""
    good=0
    bad=0
    while exercise_count<=no_exercises:
        filter = True
        while filter:
            if level == 0:
                a = random.randint(1, 8)
                b = random.randint(1, 8)
                op = random.randint(1, 2)
                if not (op == 2 and (a > 6 or b > 6)):
                    filter = False
            elif level == 1:
                a = random.randint(5, 12)
                b = random.randint(5, 12)
                op = random.randint(1, 3)
                if not ((op == 2 and (a > 10 or b > 10)) or (op == 3 and a<b)):
                    filter = False
            elif level == 2:
                a = random.randint(10, 17)
                b = random.randint(10, 17)
                op = random.randint(1, 3)
                if not ((op == 2 and (a > 15 or b > 15)) or (op == 3 and a<b)):
                    filter = False
        if op == 1:
            ops = "+"
        elif op == 2:
            ops = "*"
        elif op == 3:
            ops ="-"
        if ops == "+":
            res = a + b
        elif ops == "*":
            res = a * b
        elif ops == "-":
            res = a - b
        display.show(str(exercise_count) + ":")
        sleep(1000)
        while not button_a.was_pressed():
            display.scroll(str(a) + ops + str(b) + "=?")
            sleep(500)
        counter=0
        while not (button_a.was_pressed()):
            sleep(250)
            b_presses = button_b.get_presses()
            if b_presses >0:
                counter = counter + b_presses
            elif pin0.is_touched():
                counter = counter -1
            if counter < 10:
                display.show(str(counter))
            else:
                display.scroll(str(counter))
        if counter == res:
            display.show(Image.HAPPY)
            sleep(1000)
            good = good + 1
        else:
            display.show(Image.SAD)
            sleep(1000)
            display.show(res)
            sleep(1000)
            bad=bad + 1
        exercise_count = exercise_count+1
        result_list.append([a, b, ops, counter, res])
    result_string=result_string + "#################################\n"
    result_string=result_string + "Next game: \n"
    result_string=result_string + "Exercise level:      " + str(level+1) + "\n"
    result_string=result_string + "Number of exercises: " + str(no_exercises) + "\n"
    result_string=result_string + "Good answers:        " + str(good) + "\n"
    result_string=result_string + "Bad answers:         " + str(bad) + "\n"
    result_string=result_string + "#####################\n"
    for rl in result_list:
        result_string=result_string + str(rl[0])+rl[2]+str(rl[1])+","+str(rl[3])+","+str(rl[4])+"\n"
    
    files=os.listdir()
    exist=0
    for file in files:
        if file == "exercise.txt":
           exist=1
    if exist == 1: 
        with open("exercise.txt","r") as exercise_txt_r:
            current_string=exercise_txt_r.read()
    else:
        current_string=""
    with open("exercise.txt","w") as exercise_txt_w:
        exercise_txt_w.write(current_string + result_string)
        

    

