print("Starting")

import math

def angle_avg(a, b): # somewhat copied from stack overflow...
  a -= 128
  b -= 128
  sum_angle = ((b - a + 128) % 256 - 128) / 2
  sum_angle = (a + sum_angle + 128) % 256 - 128
  return (sum_angle + 128) 

def angle_avg_set(items):
  if not (math.log2(len(items)) % 1.0 == 0.0): # the length of the array needs to be a power of 2 because of the average weighting problem
    return -1.0
  arr = []
  item_array = items.copy()
  while len(item_array) > 0:
    arr.append(angle_avg(item_array[0], item_array[1])) # condense item_array into a new array. Average every two values
    item_array.pop(0) # remove those two values
    item_array.pop(0)
  if len(arr) == 1:
    return arr[0] # if you're fully condensed, give the final result
  return angle_avg_set(arr) # Otherwise, try again with the condensed dataset

def rolling_angle_filter(xData, data, depth_exp):
    depth = 2**depth_exp
    if len(data) < depth: # don't bother with short data
        return data
    newData = [] # new array for averaged data
    for i in range(depth, len(data) - 1):
        buffer = data[i-depth:i].copy() # get depth-length slice of data
        newData.append(angle_avg_set(buffer))
    while len(xData) > len(data):
        xData.pop(0) # make them the same length (x and y)
    return (xData, data)

import sys

sys.path.append("C:/Users/Hugh/Documents/SDAQ/Python/lib")
import graphing
from tools import *

USE_MINE = True
FILTER_EXP_DEPTH = 8
ROLLOVER_FUNCTION = apply_rollover_fix # todo rename
test_name = "Shock-Donger-HighEnd"
filename = "C:/Users/hugh/Documents/SDAQ/data/Mock R22/Calibration/High-End/" + test_name + ".sdaq"
file = open(filename, "r")

print("Begin File Read")

xData = []
yData = []

for line in file:
    if len(line) < 5:
        continue
    data = line.replace("[", "").replace("]", "").replace(",", "").replace("  ", " ").split()
    isX = True
    for p in data:
        if isX:
            xData.append(float(p))
        else:
            yData.append(int(p))
        isX = not isX

print("Calculating")

(xData, yData) = ROLLOVER_FUNCTION(xData, yData) # todo rename this crap

#(xData, yData) = rolling_angle_filter(xData, yData, FILTER_EXP_DEPTH)

print("Plotting")

plot = graphing.Plot(title=test_name, xlabel="seconds", ylabel="raw")
plot.plot(0, xData, yData)

print("Done")

input("Press ENTER to close...")