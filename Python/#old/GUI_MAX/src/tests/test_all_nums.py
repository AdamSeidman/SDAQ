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

# Segment representations for values 0-9
#            A  B  C  D  E  F  G
seg_reps = [[1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1]]


# Testing, from 0 to 19 display
for i in range(20):
    if i > 9:
        GPIO.output(12, 1)
        i %= 10
        print('.', end=' ')

    GPIO.output(display_list, seg_reps[i])

    print(i)
    time.sleep(2.5)

    GPIO.output(display_list, 0)

    GPIO.output(12, 0)

    time.sleep(0.5)

# Clears everything, including pin numbering systems
GPIO.cleanup()