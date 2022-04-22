print("Starting")

import sys

OVERRIDE_FILE_PATH = ""
PROJECT_PATH = "/SDAQ/Data/Mock R22/Calibration/"

#USER_PATH = "C:/Users/hugh/Documents"
#USER_PATH = "C:/Users/CVX32/OneDrive/Desktop/#Code"
USER_PATH = "C:/Users/Adam/Documents/#Code"

sys.path.append(USER_PATH + "/SDAQ/Python/lib")
import graphing
from tools import *

test_name = "link-4a"
#test_name = "link-5a"
#test_name = "link-5b"
#test_name = "tie-Rod"
#test_name = "Shock-Donger"
USE_HIGH_END = True

generic_name = test_name.lower().replace("-", "")
if USE_HIGH_END:
  test_name = test_name.capitalize() + "-HighEnd"
  PROJECT_PATH = PROJECT_PATH + "High-End/"
else:
  PROJECT_PATH = PROJECT_PATH + "Low-End/"
filename = USER_PATH + PROJECT_PATH + test_name + ".sdaq"
if len(OVERRIDE_FILE_PATH) > 0:
  filename = OVERRIDE_FILE_PATH

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
            xData.append(float(p))
        else:
            yData.append(int(p))
        isX = not isX

print("Calculating")

#all currently calibrated to 500 lbf (but not really because its not working)
if generic_name == "link5a":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, scale=14.3) # ??? rolling_depth=5 (different for csv?)
elif generic_name == "link4a":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, scale=1)#3.62)
elif generic_name == "link5b":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, scale=18.87)
elif generic_name == "tierod":
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData, scale=12.5)
else:
  (xData, yData, extraYData) = apply_strain_calculations(xData, yData)
  print("Not a specified link")

print("Plotting")

if not USE_HIGH_END:
  test_name = test_name + " LowEnd"

plot = graphing.Plot(title=test_name, xlabel="Time (s)", ylabel="Load (lbf)")
plot.plot(0, xData, yData)
plot.create_line(line_type=".r-")
plot.plot(1, xData, extraYData)

print("Done")

input("Press ENTER to close...")