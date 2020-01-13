#pre written shit

from wallaby import *
import os, sys
import time
import threading


class small_bot:
    #Counts
    def __init__(self):
        self.objective = 0
        #Bot movement
        self.degrees = 0
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 0
        #arms
        #sensors

class movement_thread(threading.Thread, handle):
    def __init__(self):
        self.threadid = 1
        self.name = "Movement-thread"
        #any extra functions
    def run(self):
        print("Motor Thread ready")
        move_control(handle)
        print("Finished 1")

class claw_movment_thread(threading.Thread, handle):
    def __init__(self):
        self.id = 2
        self.name = "Claw-Control"
    
    def run(self):
        print("Claw Movement ready")
        claw_control(handle)
        print("Finished 2")

class sensor_check_thread(threading.Thread, handle):
    def __init__(self):
        self.threadid = 3
        self.name = "Sensor Check"
    
    def run(self):
        print("Sensor Checking ready")
        sensor_control(handle)
        print("Finished 3")

class objective_control_thread(threading.Thread, handle):
    def __init__(self):
        self.threadid = 4
        self.name = "Objective Control"
    
    def run(self):
        print("Objectives set up")
        object_control(handle)
        print("Finished 4")

#Threading functions 
def move_control():
    print("Claw Control")
    

def claw_control():
    print("Claw Control")

def sensor_control():
    print("Sensor control")

def object_control():
    print("object control")




#100 x 130 cm
#movefunctions
    #Forward for time
def forward_time(miliseconds, speed, handle):
    if speed == 1:
        speed = 25
    elif speed == 2:
        speed = 50
    elif speed == 3:
        speed = 75
    for i in range(miliseconds):
        motor(0, speed)
        motor(1, speed)
        msleep(1)   
    motor(0, 0)
    motor(1, 0) 

    #Forward until touch sensor on
def forward_digital(sensor_number, sensor_value, handle):
    if speed == 1:
        speed = 25
    elif speed == 2:
        speed = 50
    elif speed == 3:
        speed = 75

    while digital(sensor_number) != 1:
        motor(0, speed)
        motor(1, speed)
    motor(0, 0)
    motor(1, 0) 

def backwards_time(miliseconds, speed, handle):
    if speed == 1:
        speed = 25
    elif speed == 2:
        speed = 50
    elif speed == 3:
        speed = 75
    for i in range(miliseconds):
        motor(0, speed)
        motor(1, speed)
        msleep(1)   
    motor(0, 0)
    motor(1, 0) 

    #Forward until touch sensor on
def backwards_digital(sensor_number, sensor_value, handle):
    if speed == 1:
        speed = 25
    elif speed == 2:
        speed = 50
    elif speed == 3:
        speed = 75

    while digital(sensor_number) != 1:
        motor(0, speed)
        motor(1, speed)
    motor(0, 0)
    motor(1, 0) 

def rotate(degrees_from_current, handle):
    cmpc(0)
    cmpc(1)
    #17 rotations = 1 degree
    current = handle.degrees
    rotations = degrees_from_current * 19
    if degrees_from_current > 0:
        rotations1 = 170
        rotations2 = -170
    else:
        rotations1 = -170
        rotations2 = 170
    while gmpc(0) <= rotations and gmpc(1) <= rotations:
        if gmpc(0) <= rotations:
            mav(0, rotations1)

        if gmpc(1) <= rotations:
            mav(1, rotations2)
        msleep(100)
        motor(0, 0)
        motor(0, 1)


def line_following_time(seconds):
    while seconds > 0:
        swtich = 0
        if analog(1) < 1000:
            if switch == 0:
                motor(1, 50)
                msleep(100)
                motor(1, 0)
                swtich = 1
            elif switch = 1:
                motor(0, 50)
                msleep(100)
                motor(0,0)
                switch = 0
            
        



def line_following(time_length):
    for i in range(time_length):
        if analog(5) > 1000:
            motor(1, 50)
            msleep(75)
            motor(0, 75)
            msleep(75)
        elif analog(5) < 1000:
            motor(0, 50)
            msleep(75)
            motor(1, 50)
            msleep(75)
    return 


#clawfunctions
def claw_one_reset(handle):
    enable_servos()
    set_servo_position(0,0)
    disable_servos()

def claw_one_close(handle):
    enable_servos()
    set_servo_position(0, 50)
    disable_servos()


#Sensor translations


#Objectives
    #1) drive until touch 1 activated
    #2) rotate 90 degrees (right)
    #3) close claw
    #4) reverse until touch 1 activated
    



def main():
    handle = small_bot()
    thread_motor = movement_thread(handle)
    thread_claw = claw_movment_thread(handle)
    thread_sensor = sensor_check_thread(handle)
    thread_objectives = objective_control_thread(handle)
    thread_motor.start()
    thread_claw.start()
    thread_sensor.start()
    thread_objectives.start()
    thread_motor.join()
    thread_claw.join()
    thread_sensor.join()
    thread_objectives.join()
    #wait till light
    shut_down_in(120)
    handle.objective = 1



if __name__ == "__main__":
    main()
    
