import os
import smbus
import time
def current_milli_time():
    return round(time.time() * 1000)
I2CBus = smbus.SMBus(1)
def get_i2c_data(sensors):
    global I2CBus
    data = []
    try:
        data = I2CBus.read_i2c_block_data(0x08, 0x00)
    except:
        return []
    buf = []
    for i in sensors:
        buf.append(data[i])
    return buf

current_file = None
def get_new_file(fileDir, name, ext):
    global current_file
    filename = fileDir + "/" +  name + '.' + ext
    n = 1
    while os.path.isfile(filename):
        n = n + 1
        filename = fileDir + '/' + name + '-' + str(n) + '.' + ext
    current_file = filename
    return filename

def main():
    global current_file
    data_buf = []
    max_buf = 4000
    max_size_per_file = 150 #minutes
    fileDir = '.'
    fileName = 'Link-4aLeft-LowEnd-Second'
    ext = 'sdaq'
    num_writes = 0
    get_new_file(fileDir, fileName, ext)
    while True:
        data = get_i2c_data([3])
        
        if len(data) == 0:
            continue
        print(data)
        if len(data_buf) > max_buf:
            f = open(current_file, "a")
            f.write(str(data_buf))
            f.write("\n")
            f.close()
            data_buf = []
            num_writes += 1

        if num_writes > max_size_per_file:
            get_new_file(fileDir, fileName, ext)
            num_writes = 0
        
        data_buf.append(current_milli_time())
        data_buf.append(data)
       # data_buf.append(get_i2c_data([1, 2, 3, 4, 5]))
        
main()