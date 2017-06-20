# Import GPIO
import RPi.GPIO as GPIO

# Import sleep
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
Motor1Enable = 5
Motor1B = 24
Motor1A = 27

Motor2Enable = 17
Motor2B = 6
Motor2A = 22

Motor3Enable = 12
Motor3B = 23
Motor3A = 16

Motor4Enable = 25
Motor4B = 13
Motor4A = 18

# Set up defined GPIO pins

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1Enable,GPIO.OUT) 

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2Enable,GPIO.OUT)

# Turn the motor on
GPIO.output(Motor2A,GPIO.HIGH) # GPIO high to send power to the + terminal
GPIO.output(Motor2B,GPIO.LOW) # GPIO low to ground the - terminal
GPIO.output(Motor2Enable,GPIO.HIGH) # GPIO high to enable this motor
# Leave the motor on for 3 seconds
sleep(3)

GPIO.output(Motor1A,GPIO.HIGH) # GPIO high to send power to the + terminal
GPIO.output(Motor1B,GPIO.LOW) # GPIO low to ground the - terminal
GPIO.output(Motor1Enable,GPIO.HIGH) # GPIO high to enable this motor

# Stop the motor by 'turning off' the enable GPIO pin
sleep(3)

GPIO.output(Motor2Enable,GPIO.LOW)
GPIO.output(Motor1Enable,GPIO.LOW)
# Always end this script by cleaning the GPIO
GPIO.cleanup()