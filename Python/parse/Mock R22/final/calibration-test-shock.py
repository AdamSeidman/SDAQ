import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
import graphing
from tools import *

filenames = [
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Second.sdaq", # blue
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-4aLeft-Lowend-Third.sdaq", # green
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5ALeft-Lowend-Second.sdaq", # red
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5aLeft-Lowend-Third.sdaq"#, cyan
    #"C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Link-5bRight-Lowend-Second.sdaq",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Shock-Donger-Lowend-Second.sdaq",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Shock-Donger-Lowend-Third.sdaq"
]

filenames = [
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_22_Calibration/Shock-Donger-Lowend-Second.sdaq",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/Low-End/SDLC-A.sdaq",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_cornering_1.csv",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_cornering_2.csv",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_cornering_3.csv",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_dock_drop_1.csv",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_dock_drop_2.csv",
    "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes/Raw_Strain/raw_dock_drop_3.csv"
]



plot = graphing.Plot(title="Dock Drop 2022 (FR)", xlabel="Time (s)", ylabel="Load (lbf)")
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

    scale = 1.0
    flip = True
    graph = False
    roll_depth = 400
    intercept = 0.0

    if i == 1: # todo?
        oldXdata = xData.copy()
        oldYData = yData.copy()
        xData = []
        yData = []
        for j in range(len(oldXdata)):
            if oldXdata[j] >= 29:
                xData.append(oldXdata[j] + 100)
                yData.append(oldYData[j])
            elif oldXdata[j] > 3000:
                break
        xData.insert(0, xData[0] - 26)
        yData.insert(0, yData[0])

    Is = [6]

    if i == 0:
        scale = 41.67
    elif i == 1:
        flip = False
        #scale = 14.42
        scale = 13.75
    elif i == 5:
        graph = False
    else:
        scale = 41.67
    
    if i in Is:
        graph = True
    
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
        #plot.annotate(xData[max_index], yData[max_index], xlabel="s", ylabel="lb", box_x=0.83)
    i += 1
    file.close()

input("Press ENTER to close...")