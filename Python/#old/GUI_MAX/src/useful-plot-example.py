import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()

def get_time():
    return round(time.time() * resolution) / resolution

max_seconds = 30.0
resolution = 1000
start_time = 0.0
ymax = 1.0
ymin = -1.0
extra = np.abs(ymax - ymin) * 0.1

xdata = []
ydata = []
figure, ax = plt.subplots()
lines, = ax.plot([],[], '.b-')
ax.set_autoscalex_on(True)
ax.set_ylim(ymin - extra, ymax + extra)
ax.grid()
plt.title('Values over Time')
plt.xlabel('Seconds')
plt.ylabel('Values')
start_remove = False

def plot(value):
    ydata.append(value)
    curr_time = get_time() - start_time
    xdata.append(curr_time)
    if start_remove:
        ydata.pop(0)
        xdata.pop(0)
    #Update data (with the new _and_ the old points)
    lines.set_xdata(xdata)
    lines.set_ydata(ydata)
    #Need both of these in order to rescale
    ax.relim()
    ax.autoscale_view()
    #We need to draw *and* flush
    figure.canvas.draw()
    figure.canvas.flush_events()

start_time = get_time()

for x in np.arange(0,1000000,0.1):
    if x > 1 and xdata[len(xdata) - 1] - xdata[0] > max_seconds:
        start_remove = True
    plot(np.sin(x))