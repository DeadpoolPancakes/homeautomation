#import the required modules
import RPi.GPIO as GPIO
import time

# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(18, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output (22, False)


# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output (11, False)
GPIO.output (15, False)
GPIO.output (16, False)
GPIO.output (13, False)

#raw_input('hit return key to send socket 1 ON code')
# Set K0-K3
#print "sending code 0110 1101 0101 socket 1 on"
GPIO.output (11, True)
GPIO.output (15, False)
GPIO.output (16, True)
GPIO.output (13, True)
# let it settle, encoder requires this
time.sleep(0.1)	
# Enable the modulator
GPIO.output (22, True)
# keep enabled for a period
time.sleep(0.25)
# Disable the modulator
GPIO.output (22, False)