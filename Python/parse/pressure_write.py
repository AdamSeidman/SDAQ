import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/Scripts/lib")
from tools import *

dirname = "C:/Users/Adam/Downloads/R21/mock"
filename = "raw_pressure_data.csv"

file = dirname + "/" + filename
file = open(file, "r")

xData = []
yData = []
yData2 = []

print("Collecting")

for line in file:
    if len(line) < 3:
        continue
    data = line[0:-1].replace(",", " ").split()
    xData.append(float(data[0]))
    yData.append(float(data[1]) - 128.0)
    yData2.append(float(data[2]) - 128.0)

print("Applying Fix")

yData = apply_rollover_fix(yData)

for i in range(len(yData)):
    yData[i] /= 370.5
    yData[i] *= 1820
    yData2[i] /= 370.5
    yData2[i] *= 1820
    xData[i] -= xData[2]

print("Writing")

file.close()
file = dirname + "/Brake_Pressure_R22_Mock" + ".csv"
file = open(file, "w")
file.write("Time (s),Pressure 1 (PSI),Pressure 2 (PSI)\n")

for i in range(2, len(xData) - 2):
    file.write(str(xData[i]))
    file.write(",")
    file.write(str(yData[i]))
    file.write(",")
    file.write(str(yData2[i]))
    file.write("\n")

file.close()

print("Complete!")