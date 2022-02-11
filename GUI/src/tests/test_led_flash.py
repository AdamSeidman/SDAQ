# Make sure pins are actually connected...
import RPi.GPIO as GPIO
import time

# GPIO ports
#               A   B   C   D   E   F   G
display_list = [27, 26, 25, 24, 23, 22, 13]


# Sets GPIO Mode to use GPIO pin numbering system
GPIO.setmode(GPIO.BCM)

# Sets the pins as output
GPIO.setwarnings(False)
for pin in display_list:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(True)

for i in range(200):
    GPIO.output(display_list, 1)
    GPIO.output(12, 1)
    
    time.sleep(2.5)
    
    GPIO.output(display_list, 0)
    GPIO.output(12, 0)
    
    time.sleep(2.5)
