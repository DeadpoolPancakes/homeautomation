#!/usr/bin/env python2.7

import RPi.GPIO as GPIO
import sys
import time   
from time import sleep  


try:
    import psutil
except ImportError:
    exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

GPIO.setmode(GPIO.BCM)  
  
GPIO.setup(18, GPIO.OUT)
caselight = GPIO.PWM(18, 100)       
caselight.start(0)
cpu_values = (0)              
pause_time = 1

while True:   
    try:
        cpu_values=float(psutil.cpu_percent())
        caselight.ChangeDutyCycle(cpu_values)
        time.sleep(pause_time)  

    except KeyboardInterrupt:  
        caselight.stop()              # stop the red PWM output  
        GPIO.cleanup()          # clean up GPIO on CTRL+C exit  
        quit()
