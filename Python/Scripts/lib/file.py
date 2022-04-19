import sys
sys.path.append('C:/Users/CVX32/OneDrive/Desktop/#Code/SDAQ/Python/lib')
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
filename = (r"C:\Users\CVX32\OneDrive\Desktop\SDAQ\Python\strain_gauage_data\Tie-Rod-HighEnd.sdaq")
my_title = filename[63:-5]
filename.replace("\\", "/")

# arbitrary constant of algorithm 1 (original algorithm)
constant = 75

charsToReplace = ["[", "]", ","]

with open(filename) as x:
    lines = x.readlines()

xdata = []
ydata = []

isxdata = True
datapoints = 0

# has stuff to fix & make more efficient
# but is good enough for now
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
(xdata, ydata) = funny2(xdata, ydata)
ydata = apply_rolling_filter(ydata, 5)

plot = graphing.Plot(title=my_title)
plot.plot(0, xdata, ydata)

while True:
    pass