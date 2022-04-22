print("Starting")

import sys

#sys.path.append("C:/Users/Hugh/Documents/SDAQ/Python/lib")
sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
import graphing
from tools import *

#test_name = "Shock-Donger-HighEnd"
#test_name = "Link-5A-HighEnd"
test_name = "link-4a"
generic_name = "link4a"

#filename = "C:/Users/hugh/Documents/SDAQ/data/Mock R22/Calibration/High-End/" + test_name + ".sdaq"
filename = "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/High-End/" + test_name + ".sdaq"
filename = "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Calibration/Low-End/" + test_name + ".sdaq"
#filename = "C:/Users/Adam/Documents/#Code/SDAQ/Data/Mock R22/Raw/raw_link_5A.csv"

file = open(filename, "r")

print("Begin File Read")

xData = []
yData = []

for line in file:
    if len(line) < 5:
        continue
    data = line.replace("[", "").replace("]", "").replace(",", " ").replace("  ", " ").split()
    isX = True
    for p in data:
        if isX:
            xData.append(float(p) - 1400)
        else:
            yData.append(int(p))
        isX = not isX

print("Calculating")

def apply_strain_calculations(xdata, ydata, aVal, bVal, cVal, isFlipped, dVal=400):
  (xdata, ydata) = rolling_angle_filter(xdata, ydata, aVal)
  (xdata, ydata) = basic_rollover_fix(xdata, ydata, c=128)
  extraYData = apply_rolling_filter(ydata.copy(), 1500)
  ydata = apply_rolling_filter(ydata, dVal)

  for i in range(len(ydata)):
    if isFlipped:
      ydata[i] *= -1
      extraYData[i] *= -1
    ydata[i] += bVal
    extraYData[i] += bVal
    ydata[i] *= cVal
    extraYData[i] *= cVal
  
  return (xdata, ydata, extraYData)

#all currently calibrated to 500 lbf
if generic_name == "link5a":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, 4, 180, 14.3, True)
  #(xData, yData, extraYData) = apply_strain_calculations(xData, yData, 2, 88, 1, True, dVal=5) # this is different because the range of link5a got changed (for csv)
elif generic_name == "link4a":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, 4, 80, 3.62, True)
elif generic_name == "link5b":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, 4, 64, 18.87, True)
elif generic_name == "tierod":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, 4, 168, 12.5, True)
else:
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, 4, 0, 1, True)

print("Plotting")

plot = graphing.Plot(title=test_name, xlabel="Time (s)", ylabel="Load (lbf)")
plot.plot(0, xData, yData)
plot.create_line(line_type=".r-")
plot.plot(1, xData, extraYData)

print("Done")

input("Press ENTER to close...")