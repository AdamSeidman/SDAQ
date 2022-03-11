import time
import smbus
import os.path
import RPi.GPIO as GPIO

resolution = 1000.0
start_time = 0.0

def get_time():
    global start_time
    return get_raw_time() - start_time

def get_raw_time():
    global resolution
    return (round(time.time() * resolution) / resolution)

def reset_time():
    global start_time
    start_time = get_raw_time()

current_file = ""

def get_new_file(fileDir, name, ext):
    global current_file
    if len(name) == 0:
        return current_file
    if len(fileDir) > 0:
        fileDir += "/"
    filename = fileDir + name + "." + ext
    n = 1
    while os.path.isfile(filename):
        n += 1
        filename = fileDir + name + "-" + str(n) + "." + ext
    current_file = filename
    return filename

def write(words):
    global current_file
    if len(current_file) == 0:
        return
    f = open(current_file, "a")
    f.write(words + "\n")
    f.close()

I2CBus = None

def create_i2c_bus():
    global I2CBus
    I2CBus = smbus.SMBus(1)

def get_i2c_data(addr, sensors):
    data = []
    global I2CBus
    if I2CBus is None:
        return data
    try:
        data = I2CBus.read_i2c_block_data(addr, 0x00)
    except:
        return []
    if len(sensors) > 0:
        buf = []
        for i in sensors:
            buf.append(data[i])
        data = buf
    if len(data) == 1:
        return data[0]
    return data

def get_formatted_i2c_data(addr, sensors):
    data = get_i2c_data(addr, sensors)
    if len(sensors) == 1:
        data = [addr, data]
    elif len(sensors) > 0:
        data.insert(addr, 0)
    return data

def get_active_i2c_devices():
    if I2CBus is None:
        return []
    buf = []
    for device in range(128):
        try:
            I2CBus.read_i2c_block_data(device, 0x00)
            buf.append(device)
        except:
            pass
    return buf

display_list = [27, 26, 25, 24, 23, 22, 13, 12]

def clear_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in display_list:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0);
    GPIO.setwarnings(True)
