import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/Scripts/lib")
from tools import *
import graphing

dirname = "C:/Users/Adam/Downloads/R21/mock"
filename = "raw_pressure_data.csv"

file = dirname + "/" + filename
file = open(file, "r")

xData = []
yData = []

print("Collecting")

for line in file:
    if len(line) < 3:
        continue
    data = line[0:-1].replace(",", " ").split()
    xData.append(float(data[0]))
    yData.append(float(data[1]) - 128.0)

print("Applying Fix")

yData = apply_rollover_fix(yData)

index = -1

for i in range(len(yData)):
    yData[i] /= 370.5
    yData[i] *= 1820
    if index == -1 and xData[i] > 7700:
        index = i
    xData[i] -= 7700

xData = xData[index:-1]
yData = yData[index:-1]

print("Plotting")

plot = graphing.Plot(title="Brake Pressure over Time (After Lunch)", xlabel="Seconds", ylabel="PSI")

plot.plot(0, xData, yData)

print("Complete")

input('Press ENTER to exit')