import sys

sys.path.append('C:/Users/Adam/Documents/#Code/SDAQ/Python/lib')
#sys.path.append('C:/Users/CVX32/OneDrive/Desktop/#Code/SDAQ/Python/lib')

import graphing
from tools import *

# How many datapoints wanted
# -1 for all
NUMDATAPOINTS = -1

# stuff for selecting a time frame of data
# will change to be optional later. leave at 0 and 999
MINTIME = 0
MAXTIME = 999

# have to use r"filepath" to get raw filepath & then replace \ with /
# or just highlight one \ and press ctrl-d a few times and type a single /
filename = ("C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/High-End/Link-4A-HighEnd.sdaq")
#filename = (r"C:\Users\CVX32\OneDrive\Desktop\SDAQ\Python\strain_gauage_data\Shock-Donger-HighEnd.sdaq")
my_title = filename[63:-5]
filename.replace("\\", "/")

# arbitrary constant of algorithm 1 (original algorithm)
constant = 75

charsToReplace = ["[", "]", ","]

print("Starting...")
with open(filename) as x:
    lines = x.readlines()

xdata = []
ydata = []

isxdata = True
datapoints = 0

# has stuff to fix & make more efficient
# but is good enough for now
print("Parsing File...")
for i in lines:

    linesplit = i.split()

    for j in linesplit:
        for character in charsToReplace:
            j = j.replace(character, "")

        if isxdata:
            if ((float(j) <= MINTIME) | (float(j) >= MAXTIME)): continue
            xdata.append(float(j))
            isxdata = False
        else:
            ydata.append(float(j))
            isxdata = True
            if datapoints == NUMDATAPOINTS: break
        
        if len(xdata) == len(ydata): datapoints += 1
        

    if datapoints == NUMDATAPOINTS: break

# choose what algorithm is wanted here
print("Calculating...")

(xdata, ydata) = apply_rollover_fix(xdata, ydata, filterOutliers=True, outlier_constant=30, filter_constant=75)
#(xdata, ydata) = rolling_angle_filter(xdata, ydata, 6)
(xdata, ydata) = apply_rollover_fix(xdata, ydata, filterOutliers=False, filter_constant=75)
#more math

print("Plotting...")
plot = graphing.Plot(title=my_title)
plot.plot(0, xdata, ydata)
    
input("Press ENTER to close...")