# Make sure pins are actually connected...
import RPi.GPIO as GPIO
import time

# GPIO ports
#               A   B   C   D   E   F   G
display_list = [27, 26, 25, 24, 23, 22]

# Sets GPIO Mode to use GPIO pin numbering system
GPIO.setmode(GPIO.BCM)

# Sets the pins as output
GPIO.setwarnings(False)
for pin in display_list:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setwarnings(True)

while True:
    for i in range(len(display_list)):
        
        GPIO.output(display_list[i], 1)
        time.sleep(1)
    
        GPIO.output(display_list[i], 0)
        
    GPIO.output(display_list, 0)

