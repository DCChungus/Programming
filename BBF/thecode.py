#!/usr/bin/python
import os, sys
from wallaby import *
import time

#Ports
line_sensor = 1
#et_sensor = ?

#Left motor = 0 red
#Right motor = 1 black 
#Claw servo = 1
#scoop servo = 0
#arm servo = 

#touch sensors? 


#Main Code handler
def main():
    disable_servos()
    enable_servos()
    #claw values
    grab = 
    corner = 
    unused = 
    down_grab =
    half_finish =
    finish = 
    #scoop values
    start_x =
    x1 =
    x2 = ...
    last_x = 
    dump_x = 

    #arm values
    start_y =
    y1 = ...
    lasty =
    finish_y = 
    dump_y =
    set_arm_x(start_x)
    set_arm_y(start_y)

    #Change?
    set_claw(unused)

    #Light wait
    set_claw(grab)
    forward_time(2500)
    slow_claw(grab, half_corner)
    forward_time(200)
    slow_claw(half_corver, grab)
    set_claw(unused)
    while analog(line_sensor) < 1900:
        rotate_to_find(-1)
    motors_off()
    rotate(10)
    #may need to change
    line_follow_forward()
    #Sensor here?
    rotate(-5)
    while analog(line_sensor) < 1900:
        rotate_to_find(-1)
    motors_off()
    #Sensor here?
    line_follow_Platform()
    for i in range(2):
        slow_x(star_x, x1)
        slow_y(start_y, y1)
        #.....
    #backwards line follow to ramp
    rotate(-5)
    while analog(line_sensor) < 1900:
        rotate(-1)
    #forward line follow timed
    set_claw(down_grab)
    forward_time(500)
    slow_claw(down_grab, half_finish)
    slow_claw(half_finish, finish)
    slow_y(last_y, dump_y)
    slow_x(last_x, dump_x)
    slow_claw(half_finish, finish)
    forward_time(500)
    rotate(90)
    #How grab?
    forward_time(2500)
    disable_servos()



    

#Motor off
def motors_off():
    motor(0, 0)
    motor(1, 0)
    msleep(50)



#forward functions
def forward_time(ms):
    motor(0, 100)
    motor(1, 100)
    msleep(ms)
    motors_off()

def forward_line():
    motor(0, 100)
    motor(1, 95)
    msleep(10)

#backwards functions
def backward_time(ms):
    motor(0, -100)
    motor(1, -100)
    msleep(ms)
    motors_off()

def backwards():
    motor(0, -100)
    motor(1, -95)
    msleep(10)

#Rotation set
def rotate(degrees):
    cmpc(0)
    cmpc(1)
    #degree to rotation translation
    rotations = degrees*25

    if degrees > 0:
        left_speed = 
        right_speed =
        right_rotations = gmpc(1)

    if degrees < 0:
        left_speed = 
        right_speed =
        right_rotations = gmpc(1)

    while True:
        mav(0, left_speed)
        mav(1, right_speed)
        msleep(100)
        if gmpc(1) < int(rotations):
            break
    motors_off()

#rotation find
def rotate_to_find(degrees):
    cmpc(0)
    cmpc(1)
    #degrees to rotation
    rotations = degrees*25

    if degrees > 0:
        left_speed = 
        right_speed =
        right_rotations = gmpc(1)

    if degrees < 0:
        left_speed = 
        right_speed =
        right_rotations = gmpc(1)

    while True:
        mav(0, left_speed)
        mav(1, right_speed)
        msleep(100)
        if gmpc(1) < int(rotations):
            break
#claw
def set_claw(position):
    set_servo_position(3, position)
    return

def slow_claw(position1, position2):
    change = position2 - position1
    if change > 0:
        current_position = position1
        while current_position < position2:
            set_claw(current_position)
            current_position += 5
            msleep(5)
        return


    elif change < 0:
        current_position = position1
        while current_position > position2:
            set_claw(current_position)
            current_position -= 5
            msleep(5)
        return
    
    else:
        return


#Arm
def set_arm_y(position):
    set_servo_position(1, position)
    return



def slow_y(position1, position2):
    change = position2 - position1
    if change > 0:
        current_position = position1
        while current_position < position2:
            set_arm_y(current_position)
            current_position += 5
            msleep(10)
        return


    elif change < 0:
        current_position = position1
        while current_position > position2:
            set_arm_y(current_position)
            current_position -= 5
            msleep(10)
        return
    
    else:
        return

#scoop
def set_arm_x(position):
    set_servo_position(0, position)

def slow_x(position1, position2):
    change = position2 - position1
    if change > 0:
        current_position = position1
        while current_position < position2:
            set_arm_x(current_position)
            current_position += 5
            msleep(5)
        return


    elif change < 0:
        current_position = position1
        while current_position > position2:
            set_arm_x(current_position)
            current_position -= 5
            msleep(5)
        return
    
    else:
        return



def line_follow_forward():
    while digital(0)==0:
        if analog(2)<1000:
            motor(1,100)
            motor(2,85)
            msleep(10)
        else:
            motor(1,85)
            motor(2,100)
            msleep(10)

    motor(1,100)
    motor(2,-100)
    msleep(500)
    while analog(2)<1000:
        motor(1,100)
        motor(2,-100)

def line_follow_Platform():
    i=0
    while i < 500:
         if analog(2)<1000:
            motor(1,100)
            motor(2,85)
            msleep(10)
            i = i + 1
        else:
            motor(1,85)
            motor(2,100)
            msleep(10)
            i = i + 1


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();