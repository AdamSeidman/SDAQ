import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/Scripts/lib")
from tools import *

file = "C:/Users/Adam/Downloads/R20/Mock/test.csv"

print("Starting")

file = open(file, "r")

xData = [0]
yData = [0]
yData2 = [0]

print("Reading")

for line in file:
    data = line.replace(",", " ").replace("  ", " ").split()
    if len(data) < 5:
        continue
    xData.append(float(data[0]))
    yData.append(float(data[2]))
    yData2.append(float(data[4]))

print("Filtering")

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
yData2 = apply_rolling_filter(yData2, 7)

vel = [0]
vel2 = [0]

print("Calculating 1")

for i in range(1, len(yData)):
    vel.append(get_velocity(yData[i], xData[i], xData[i-1]))

print("Calculating 2")

shift_reg = 0
for i in range(1, len(yData2)):
    vel2.append(get_velocity(yData2[i], xData[i], xData[i-1]))

xData = xData[10:-1]
#yData = yData[10:-1]
#yData2 = yData2[10:-1]
vel = vel[10:-1]
vel2 = vel2[10:-1]

print("Writing")

file.close()
file = "C:/Users/Adam/Downloads/R20/Mock/" + "Shock_Velocities_R20_Mock" + ".csv"
file = open(file, "w")

file.write("Time (s),Rear Right (in/s),Front Left (in/s)\n")

for i in range(len(xData)):
    file.write(str(xData[i]))
    file.write(",")
    file.write(str(vel[i]))
    file.write(",")
    file.write(str(vel2[i]))
    file.write("\n")

file.close()

print("Complete!")
