import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
import graphing
from tools import *

filenames = [
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Second.sdaq", # blue
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Third.sdaq", # green
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5ALeft-Lowend-Second.sdaq", # red
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5aLeft-Lowend-Third.sdaq"#, cyan
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5bRight-Lowend-Second.sdaq",
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Shock-Donger-Lowend-Second.sdaq",
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Shock-Donger-Lowend-Third.sdaq"
]

filenames = [
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Second.sdaq", # blue
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Third.sdaq", # green
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/High-End/Link-4A-HighEnd.sdaq", # red
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/Low-End/link-4a.sdaq"#, cyan
]


filenames = [
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/Low-End/link-5a.sdaq", # blue
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/High-End/Link-5A-HighEnd.sdaq", # green
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5ALeft-Lowend-Second.sdaq", # red (green)
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5aLeft-Lowend-Third.sdaq", # cyan
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Raw/raw_link_5A.csv" #c
]


plot = graphing.Plot(title="Link 5A Mock Endurance", xlabel="Time (s)", ylabel="Load (lbf)")
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
                xData.append(float(item))
            else:
                yData.append(int(item))
            isX = not isX

    if i == 3:
        oldXdata = xData.copy()
        oldYData = yData.copy()
        xData = []
        yData = []
        for j in range(len(oldXdata)):
            if oldXdata[j] > -1:
                xData.append(oldXdata[j])
                yData.append(oldYData[j])
            elif oldXdata[j] > 3000:
                break

    scale = 1.0
    flip = True
    graph = False
    roll_depth = 400
    intercept = 0.0

    if i == 0:
        flip = False
        scale = 2.78
    elif i == 1:
        scale = 5.0
    elif i == 2:
        flip = False
        scale = 21.9
    else:
        graph = True
        scale = 5.0
        intercept = 8.8
        roll_depth = 0

    (xData, yData, extraData) = apply_strain_calculations(xData, yData, isFlipped=flip, scale=scale, rolling_depth=roll_depth, intercept=intercept, angle_depth=2)


    if graph:
        #plot = graphing.Plot(title=filename[57:-5], xlabel="Time (s)")
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