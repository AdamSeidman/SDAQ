# feck max
import RPi.GPIO as GPIO

# GPIO ports
#               A   B   C   D   E   F   G   h
display_list = [27, 26, 25, 24, 23, 22, 13, 12]

# Sets GPIO Mode to use GPIO pin numbering system
GPIO.setmode(GPIO.BCM)

# Sets the pins as output
GPIO.setwarnings(False)
for pin in display_list:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0);
GPIO.setwarnings(True)

