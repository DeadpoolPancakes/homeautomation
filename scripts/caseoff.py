import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
red = GPIO.PWM(18, 100)
red.start(0)
GPIO.cleanup()