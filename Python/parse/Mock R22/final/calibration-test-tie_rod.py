import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
import graphing
from tools import *

filenames = [
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/Low-End/tie-Rod-A.sdaq"
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Raw/raw_tie_rod_mock.csv"
]


plot = graphing.Plot(title="Tie Rod Mock Endurance", xlabel="Time (s)", ylabel="Load (lbf)")
i = 0

for filename in filenames:
    file = open(filename, "r")
    xData = []
    yData = []

    for line in file:
        data = line.replace("[", "").replace("]", "").replace(",", " ").replace("  ", " ").split()
        isX = True
        for item in data:
            if isX:
                #print("x: " + item)
                xData.append(float(item))
            else:
                #print("y: " + item)
                yData.append(int(item))
            isX = not isX

    scale = 0.69
    flip = True
    graph = True
    roll_depth = 400
    intercept = 0.0

    if i == 0:
        roll_depth = 150

    index = 0
    for j in range(len(xData)):
        if xData[j] > 1500:
            index = j
            break

    xData = xData[index:-1]
    yData = yData[index:-1]

    (xData, yData, extraData) = apply_strain_calculations(xData, yData, isFlipped=flip, scale=scale, rolling_depth=roll_depth, intercept=intercept, angle_depth=4)

    if graph:
        if not (i == 0):
            plot.create_line(line_type="")
        
        plot.plot(i, xData, yData)
        ymax = yData[0]
        max_index = 0
        for index in range(1, len(xData)):
            if yData[index] > ymax:
                max_index = index
                ymax = yData[index]

        plot.annotate(xData[max_index], yData[max_index], xlabel="s", ylabel="lb")
    i += 1
    file.close()

input("Press ENTER to close...")