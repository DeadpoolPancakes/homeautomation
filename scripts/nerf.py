#import the required modules
import RPi.GPIO as GPIO
import time

# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT)

GPIO.output (18, True)

# let it settle, encoder requires this
time.sleep(1)	
# Enable the modulator
GPIO.output (18, False)