import smbus
import time

def scan():
    I2Cbus = smbus.SMBus(1)
    active_buses = []

    for device in range(128):
        try:
            I2Cbus.read_byte(device)
            active_buses.append(device)
            print(device)
        except:
            pass

    print(active_buses)
    return active_buses