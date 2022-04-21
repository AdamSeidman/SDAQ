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
  while len(items) > 0:
    arr.append(angle_avg(items[0], items[1])) # condense items into a new array. Average every two values
    items.pop(0) # remove those two values
    items.pop(0)
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

#colins (slightly modified to pass through xData)
def rolling_angle_filter2(xData, data, depth_exp, c=64):
    depth = 2**depth_exp
    if len(data) < depth:
        depth = len(data)
    buffer = data[0:depth]
    #print(len(data))
    for i in range(len(data)):
        #print(i, ",", (i % depth), ",", len(data), ",", len(buffer))
        buffer[i % depth] = data[i]
        if i < c:
            data[i] = angle_avg_set(buffer[i:i+c]) # this comes from prev message
        else:
            data[i] = angle_avg_set(buffer[i-c:i+c]) # this comes from prev message
        print(data[i])
    return (xData, data)

import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/Scripts/lib")
import graphing
from tools import *

USE_MINE = False
FILTER_EXP_DEPTH = 4
ROLLOVER_FUNCTION = funny2 # todo rename
test_name = "Link-4A-HighEnd"
filename = "C:/Users/Adam/Documents/#Code/SDAQ/Python/strain_gauage_data/" + test_name + ".sdaq"
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

if USE_MINE:
    (xData, yData) = rolling_angle_filter(xData, yData, FILTER_EXP_DEPTH)
else:
    (xData, yData) = rolling_angle_filter2(xData, yData, FILTER_EXP_DEPTH)

print("Plotting")

plot = graphing.Plot(title=test_name, xlabel="seconds", ylabel="raw")
plot.plot(0, xData, yData)

print("Done")

input("Press ENTER to close...")