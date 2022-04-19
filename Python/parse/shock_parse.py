import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/Scripts/lib")
import graphing
from tools import *

file = "C:/Users/Adam/Downloads/R20/Mock/test.csv"

print("Starting")

file = open(file, "r")

xData = [0]
yData = [0]

print("Reading")

item = 1
minTime = 1650
duration = 30

for line in file:
    data = line.replace(",", " ").replace("  ", " ").split()
    if len(data) < (item + 1):
        continue
    time = float(data[0])
    if time > minTime and time < (minTime + duration):
        xData.append(time - minTime)
        yData.append(float(data[item]))

print("Calculating")

shift_reg = 0
def get_position(filtered_val):
    return (5 - (5 * (filtered_val / 255))) * 1.7716
def get_velocity(filtered_val, current_time, prev_time):
    global shift_reg
    val = get_position(filtered_val)
    val2 = val - shift_reg
    shift_reg = val
    return val2 * (1 / (current_time-prev_time))

yData = apply_rolling_filter(yData, 7)

vel = [0]

for i in range(1, len(yData)):
    vel.append(get_velocity(yData[i], xData[i], xData[i-1]))

print("Plotting")

plot = graphing.Plot(title="shock velocity", xlabel="seconds", ylabel="in/s")
plot.plot(0, xData[10:-1], vel[10:-1])

input("Press ENTER to close...")
