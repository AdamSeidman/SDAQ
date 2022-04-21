import smbus
import time

def read(int bus_addr):
	I2Cbus = smbus.SMBus(1)

	try:
		data = I2Cbus.read_i2c_block_data(bus_addr, 0x00)
	except:
		print("error")
		time.sleep(0.5)
	
	print(data)
	return data

