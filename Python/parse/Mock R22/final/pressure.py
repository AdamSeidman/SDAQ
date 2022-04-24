import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
from tools import *
import graphing

dirname = "C:/Users/Adam/Downloads/R21/mock"
filename = "raw_pressure_data.csv"
my_title="Brake Pressure: Mock Endurance 2022"

orig_csv = True
sensor_number = 3
num_sensors = 3
replace_char = " "

file = dirname + "/" + filename
''''''
#file = "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/BrakeCheck.sdaq"
#my_title="Brake Check Pressure 2022"

#file = "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Cornering.sdaq"
#my_title="Brake Pressure: Cornering 2022"
''''''
file = open(file, "r")

xData = []
yData = []

print("Collecting")

start_time = -1
raw_start_time = -1

for line in file:
    if len(line) < 3:
        continue

    data = line.replace(",", replace_char).replace("[", replace_char).replace("]", replace_char).replace("  ", " ").split()

    if raw_start_time == -1:
        raw_start_time = float(data[0])

    if float(data[0]) - raw_start_time > 5000:#< 10000:
        continue
        #pass

    if start_time == -1:
        start_time = float(data[0])

    if orig_csv:
        xData.append(float(data[0]) - start_time)
        yData.append(float(data[1]))
    else:
        for i in range(len(data)):
            if i % (num_sensors + 1) == 0:
                xData.append(float(data[i]) - start_time)
                xData[len(xData) - 1] /= 1000.0
            elif i % (num_sensors + 1) == sensor_number:
                yData.append(float(data[i])  - 128.0)

print("Applying Fix")

yData = brakes_rollover_fix(yData)

index = -1

for i in range(len(yData)):
    #if xData[i] > 5000:
    #    continue
    
    yData[i] /= 370.5
    yData[i] *= 1820
    if index == -1 and xData[i] > 5000:
        index = i
    #xData[i] -= 7700

#xData = xData[index:-1]
#yData = yData[index:-1]

#xData = xData[0:index]
#yData = yData[0:index]

print("Plotting")

plot = graphing.Plot(title=my_title, xlabel="Seconds", ylabel="PSI")

plot.plot(0, xData, yData)

max_val = max(yData)
index = 0
for i in range(len(xData)):
    if yData[i] == max_val:
        index = i
        break

plot.annotate(xData[index], max_val, xlabel=" s", ylabel=" psi")

print("Complete")

input('Press ENTER to exit')