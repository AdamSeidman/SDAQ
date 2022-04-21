import smbus
import time

I2Cbus = smbus.SMBus(1)
active_busses = []

for device in range(128):
    try:
        I2Cbus.read_byte(device)
        active_busses.append(device)
        print(device)
    except:
        pass

print(active_busses)
time.sleep(0.5)

while True:
	try:
		data = I2Cbus.read_i2c_block_data(active_busses[0], 0x00)
		print("recv from slave: ")
		print(data)
	except:
		print("error")
		time.sleep(0.5)

