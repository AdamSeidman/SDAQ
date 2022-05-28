import matplotlib.pyplot as plt
import numpy as np
import time
import smbus
import threading

plt.ion()

def get_time():
    return round(time.time() * resolution) / resolution

max_seconds = 30.0
resolution = 1000
start_time = 0.0
ymax = 256.0
ymin = 0.0
extra = np.abs(ymax - ymin) * 0.1

xdata = []
ydata = []
figure, ax = plt.subplots()
lines, = ax.plot([],[], '.b-')
ax.set_autoscalex_on(True)
ax.set_ylim(ymin - extra, ymax + extra)
ax.grid()
plt.title('Raw Analog Value Over Time')
plt.xlabel('Seconds')
plt.ylabel('Values')
start_remove = False

def plot():
    #print(len(xdata))    
    lines.set_xdata(xdata)
    lines.set_ydata(ydata)
    ax.relim()
    ax.autoscale_view()
    figure.canvas.draw()
    figure.canvas.flush_events()

I2Cbus = smbus.SMBus(1)

start_time = get_time()

i = 0

def yeet(a, b):
    while True:
        plot()

threading.Thread(target=yeet, args=(1,2)).start()

while True:
    #if True:
    try:
        data = I2Cbus.read_i2c_block_data(0x08, 0x00)[1]
        i = i + 1  
        ydata.append(data)
        curr_time = get_time() - start_time
        xdata.append(curr_time)
        if (len(xdata) > 4 and xdata[len(xdata) - 1] - xdata[0] > max_seconds):
            ydata.pop(0)
            xdata.pop(0)
        #if i % 100 == 0:
        #    threading.Thread(target=plot, args=(data,"")).start()
        print(str(i) + " " + str(get_time() - start_time) + " " + str(data))
    except:
        print("error")