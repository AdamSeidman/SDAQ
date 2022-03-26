import sys
import smbus
import time

I2Cbus = smbus.SMBus(1)

time.sleep(0.5)

while True:
	try:
		data = I2Cbus.read_i2c_block_data(0x11, 0x00)
		print("recv from slave: ")
		print(data)
	except:
		print("error")
		time.sleep(0.5)



