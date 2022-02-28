import matplotlib.pyplot as plt
import numpy as np
import time
import smbus

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

def plot(value):
    ydata.append(value)
    curr_time = get_time() - start_time
    xdata.append(curr_time)
    if start_remove or (len(xdata) > 4 and xdata[len(xdata) - 1] - xdata[0] > max_seconds):
        ydata.pop(0)
        xdata.pop(0)
        start_remove = True
    #Update data (with the new _and_ the old points)
    lines.set_xdata(xdata)
    lines.set_ydata(ydata)
    #Need both of these in order to rescale
    ax.relim()
    ax.autoscale_view()
    #We need to draw *and* flush
    figure.canvas.draw()
    figure.canvas.flush_events()

I2Cbus = smbus.SMBus(1)

start_time = get_time()

while True:
	try:
		data = I2Cbus.read_i2c_block_data(0x08, 0x00)[0]
		plot(data)
	except:
		print("error")
		time.sleep(0.5)