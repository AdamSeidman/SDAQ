import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
import graphing
from tools import *

file = "C:/Users/Adam/Downloads/R20/Mock/test.csv"
file = "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_LPot/raw_dock_drop_2.csv"

print("Starting")

file = open(file, "r")

xData = [0]
yData = [0]

print("Reading")

item = 1
minTime = 0
duration = 90

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

start_plot_index = 10

plot = graphing.Plot(title="Dock Drop 2022 (FR)", xlabel="Time (s)", ylabel="Velocity (in/s)")
plot.create_line(line_type=".k-")
plot.plot(1, xData[start_plot_index:-1], vel[start_plot_index:-1])

ymax = vel[start_plot_index]
max_index = start_plot_index
for index in range(start_plot_index + 1, len(xData)):
    if vel[index] > ymax:
        max_index = index
        ymax = vel[index]

plot.annotate(xData[max_index], vel[max_index], xlabel=" s", ylabel=" in/s")

input("Press ENTER to close...")
