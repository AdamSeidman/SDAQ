import ast
from statistics import median, quantiles
import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
path = path + "..\\..\\..\\lib"
path = os.path.abspath(path)
sys.path.append(path)
import graphing

from tools import *
class HeatData:
    def __init__(self, arr):
        self.time = arr[0]
        self.therms = arr[1]
    def change_therm_val(self, index : int, func) -> None:
        self.therms[index] = func(self.therms[index])
    def get_therm(self, index : int) -> float:
        return self.therms[index]
    def get_time(self) -> int:
        return self.time

def HeatDumpMillis(arr):
    heatDumps = []
    for val in arr:
        time = val.get_time()
        heatDumps.append(time)
    return heatDumps
def HeatDumpTherms(arr, num):
    heatDumps = []
    for val in arr:
        heatDumps.append(val.get_therm(num))
    return heatDumps
file = open("C:\\Users\\hugh\\Downloads\\heat\\heat\\testing.sdaq", "r")
file2 = open("C:\\Users\\hugh\\Downloads\\EGP0530J103-REV-0.csv")
lines = file.readlines()
lines2 = file2.readlines()
heatData = []
itemList = []
for line in lines:
    thing = ast.literal_eval(line)
    for i in range(0, int(len(thing) / 2), 2):
        heatData.append(HeatData(thing[i:i + 2]))
for line in lines2:
    thingarr = line.split(',')
    itemList.append([float(thingarr[0]), float(thingarr[1])])
itemList.sort(key=lambda x: x[0])
curve = dict()
for item in itemList:
    curve[float(item[0])] = float(item[1])
heatData.sort(key=lambda x: x.get_time())
plt = graphing.Plot(title="TestData", xlabel="Time (millis)", ylabel="Temperature")
time = HeatDumpMillis(heatData)
start = time[0]
for i in range(0, len(time)):
    time[i] = time[i] - start

def conv_arr_to_volts(arr):
    for i in range(len(arr)):
        arr[i] = convert_num_to_volt(arr[i], 5, 10)
    return arr
def conv_arr_volts_to_r(arr):
    for i in range(len(arr)):
        arr[i] = find_resistance_in_divider(5, arr[i], 5000)
    return arr
def conv_arr_r_to_curve(arr):
    for i in range(len(arr)):
        arr[i] = curve.get(list(curve)[binary_search_approximate_match(list(curve), arr[i])])
    return arr
def fast_conv_arr_to_val(arr):
    for i in range(len(arr)):
        arr[i] = curve.get(list(curve)[binary_search_approximate_match(list(curve), find_resistance_in_divider(5, convert_num_to_volt(arr[i], 5, 10), 5000))])
    return arr
def conv_arr_to_val(arr):
    return conv_arr_r_to_curve(conv_arr_volts_to_r(conv_arr_to_volts(arr)))
def purge_outliers(arr, rang):
    newArr = []
    for i in range(len(arr)):
        lowEnd = i - rang
        highEnd = i + rang
        if lowEnd < 0:
            lowEnd = 0
        if highEnd > len(arr):
            highEnd = len(arr)
        quarts = quantiles(arr[lowEnd : highEnd], n=4)
        IQR = quarts[2] - quarts[1]
        med = median(arr[lowEnd : highEnd])
        isBelowTop = ((med + 1.5 * IQR) > arr[i])
        isAboveBottom = ((med - 1.5 * IQR) < arr[i])
        if (isBelowTop and isAboveBottom or med == arr[i]):
            pass
        else:
            newArr.append(i)
    return newArr
def removeNums(arr : list, x : list, y : list):
    xcopy = []
    ycopy = []
    for i in range(max(len(x), len(y))):
        if i in arr:
            pass
        else:
            xcopy.append(x[i])
            ycopy.append(y[i])
    return [xcopy, ycopy]
def rolling_average(arr):
    internal = arr.copy()
    rang = 5
    for i in range(rang, len(internal) - rang):
        lowEnd = i - rang
        highEnd = i + rang
        if lowEnd < 0:
            lowEnd = 0
        if highEnd > len(internal):
            highEnd = len(internal)
        temp = arr[lowEnd : highEnd]
        val = 0
        for i in range(len(temp)):
            val = val + temp[i]
        avg = val / len(temp)
        internal[i] = avg
    return internal
firstTherms = fast_conv_arr_to_val(HeatDumpTherms(heatData, 0))
removals = purge_outliers(firstTherms, 15)
[time0, y] = removeNums(removals, time, firstTherms)
plt.plot(0, time0, rolling_average(y))
secondTherms = fast_conv_arr_to_val(HeatDumpTherms(heatData, 1))
[time1, secondTherms] = removeNums(purge_outliers(secondTherms, 15), time, secondTherms)
plt.plot(1, time1, rolling_average(secondTherms))
thirdTherms = fast_conv_arr_to_val(HeatDumpTherms(heatData, 2))
[time2, thirdTherms] = removeNums(purge_outliers(thirdTherms, 15), time, thirdTherms)
plt.plot(2, time2, rolling_average(thirdTherms))
input("Press ENTER to close...")