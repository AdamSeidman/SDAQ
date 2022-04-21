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


# Displays numbers, I think
def num_to_display(num):

    # Sets limit for the number
    if num < 0:
        num = 0
    elif num > 19:
        num = 19

    # Turns on the dot on display for numbers higher than 9
    if num > 9:
        GPIO.output(12, 1)
        print('.', end=' ')

        # Adjusts for the dot display
        num %= 10

    # Turns on segments to display the number
    GPIO.output(display_list, seg_reps[num])
    print(num)

    time.sleep(2.5)

    # Turns off every segment on the display
    GPIO.output(12, 0)
    GPIO.output(display_list, 0)

    # Clears everything, including pin numbering systems
#    GPIO.cleanup()

# num_to_display(-5)
# num_to_display(21)
# num_to_display(7)
