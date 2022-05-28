import time
import smbus
import os.path

testname = "Shock-Donger-Lowend-Third"

def get_time():
    return round(time.time() * resolution) / resolution

resolution = 1000
start_time = 0.0

I2Cbus = smbus.SMBus(1)
start_time = get_time()

buffer = []

ext = ".sdaq"
filename = testname + ext
i = 1

while os.path.isfile(filename):
    print(i)
    i = i + 1
    filename = testname + str(i) + ext

f = open(filename, "w")
f.close()

def fwrite(value):
    f = open(filename, "a")
    f.write(str(value) + "\n")
    f.close()

max_buf_length = 2000

def bufWrite(addr, sensors):
    try:
        global buffer
        data = I2Cbus.read_i2c_block_data(addr, 0x00)
        if len(sensors) > 0:
            buf = []
            for i in sensors:
                buf.append(data[i])
            data = buf
        curr_time = get_time() - start_time
        buffer.append(curr_time)
        buffer.append(data)
        if len(sensors) > 0:# and len(buffer) % 500 == 0:
            print(formatNumber(curr_time) + " s    \t" + str(data))
        if len(buffer) >= max_buf_length:
            fwrite(buffer)
            if len(sensors) == 0:
                print(buffer)
            buffer = []
    except:
        pass

def formatNumber(n):
    n = n * 100
    return str((n - (n % 1)) / 100)

while True:
     bufWrite(0x08, [3])
     #bufWrite(0x09, [1])