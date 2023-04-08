import smbus
import RPi.GPIO as GPIO

I2CBus = None

def create_i2c_bus():
    global I2CBus
    I2CBus = smbus.SMBus(1)

def get_i2c_data(addr: int, sensors: "list[int]") -> "int | list[int]":
    data = []
    global I2CBus
    if I2CBus is None:
        return data
    try:
        data = I2CBus.read_i2c_block_data(addr, 0x00)
        ID = data[0]
        vals = []
        vals.append(data[0])
        for i in range(1, len(data) - 1, 2):
            vals.append(data[i] + (data[i + 1] << 8)) # normalize with new board file to allow for multi-pickup
        data = vals
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
        GPIO.output(pin, 0)
    GPIO.setwarnings(True)
