import time
import os.path
from tkinter.filedialog import askdirectory
import math
from math import *
def get_directory():
    dirname = askdirectory() # + "/"
    if dirname == None or len(dirname) < 1:
        dirname = "./"
    return dirname

def get_num_of_files(dirname):
    total_files = len([name for name in os.listdir(dirname)
                       if os.path.isfile(os.path.join(dirname, name)) and name != 'log.txt'])
    
    return total_files

def is_number(num):
    return isinstance(num, int)


def convert_num_to_volt(num : int, max_voltage : float, bits : int):
    """
    This function does conversion from a number to voltage
    num (int): the voltage from the ADC to convert into an actual voltage
    max_voltage (float): The maximum voltage you're comparing
    bits (int): the number of bits in the ADC
    """
    return num * max_voltage / 2**bits
def find_resistance_in_divider(Vin : float, Vout: float, R2 : float):
    return (Vin / Vout * R2) - R2
def binary_search_approximate_match(arr : list, val : float):
    low = 0
    high = len(arr) - 1
    mid = 0
    closest = (high + low) // 2
 
    while low <= high:
        
        mid = (high + low) // 2
        useful = arr[mid]
        distance1 = fabs(arr[mid] - val) 
        distance2 = fabs(arr[closest] - val)
        if distance1 < distance2:
            closest = mid
        # If x is greater, ignore left half
        if arr[mid] < val:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > val:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return closest
def convert_ticks_to_rpm(ticks, tpr, inverted=False):
    xData = [0]
    yData = [0]
    lastTickTime = -1000.0
    lastTick = 0
    for tick in ticks:
        if inverted:
            if not (tick[0] == lastTick):
                xData.append(tick[1])
                yData.append((((1.0 / (tick[1] - lastTickTime)) * 60.0) / tpr))
                lastTickTime = tick[1]    
        else:
            # list of valid tick values depending on what's going on for NO type hall effect sensors
            if not (tick[0] == lastTick) and (tick[0] in [255, 1, 1024]):
                xData.append(tick[1])
                yData.append((((1.0 / (tick[1] - lastTickTime)) * 60.0) / tpr))
                lastTickTime = tick[1]
        lastTick = tick[0]
    return (xData, yData)

def pad_both_sides_of_text(text, num=8):
    pad = num - len(text)
    left = num // 2
    right = num - left
    
    left_pad = left * " "
    right_pad = right * " "
    
    return left_pad + text + right_pad

def pad_text(text, num=8, is_right=True):
    pad = (num - len(text)) * " "
    if is_right:
        return text + pad
    return pad + text

def apply_rolling_filter(data, depth):
    if len(data) < depth:
        depth = len(data)
    buffer = data[0:depth]
    for i in range(len(data)):
        buffer[i % depth] = data[i]
        data[i] = (sum(buffer) / len(buffer))
    return data

def basic_rollover_fix(xData, yData, c=150):
    if len(xData) <= 2:
        return (xData, yData)
    newXData = []
    newYData = []
    adjuster = 0
    for i in range(1, len(yData)):
        diff = yData[i-1] - yData[i]
        if diff < (-1 * c):
            adjuster -= 256
        elif diff > c:
            adjuster += 256
        newXData.append(xData[i])
        newYData.append(yData[i] + adjuster)
    return (newXData, newYData)

# original rollover fix algorithm
def brakes_rollover_fix(data, c=75):
    if len(data) <= 2:
        return data
    lastVal = data[0]
    for i in range(1, len(data)):
        ndiff = abs(lastVal - (data[i] - 255))
        diff = abs(lastVal - data[i])
        pdiff = abs(lastVal - (data[i] + 255))
        dmin = min(ndiff, diff, pdiff)
        if abs(dmin - diff) > c:
            if ndiff == dmin:
                for n in range(i, len(data)):
                    data[n] -= 255
            elif pdiff == dmin:
                for n in range(i, len(data)):
                    data[n] += 255
        lastVal = data[i]
    return data

def apply_calibration(data, min_val, max_val):
    data_min = min(data)
    data_max = max(data)
    return [(((max_val - min_val) * ((x - data_min) / (data_max - data_min))) + min_val) for x in data]

def shift_around_val(data, val, extra=0):
    for index in range(len(data)):
        ydata = data[index][1]
        num = 0
        for i in range(len(ydata)):
            if ydata[i] >= val:
                num = data[index][0][i]
                break
        xdata = []
        for i in range(len(ydata)):
            xdata.append(((data[index][0][i]) - num) + extra)
        data[index][0] = xdata
    return data

def combine_data(data):
    buf = [[], []]
    while len(data) > 0:
        min_num = 999999
        for arr in data:
            min_num = min(min_num, arr[0][0])
        for i in range(len(data)):
            if data[i][0][0] == min_num:
                buf[0].append(data[i][0][0])
                buf[1].append(data[i][1][0])
                data[i][0].pop(0)
                data[i][1].pop(0)
                if len(data[i][0]) == 0:
                    data.pop(i)
                break
    return buf

def apply_cutoff(data, val):
    while len(data[0]) > 0 and data[0][0] < val:
        #print(data)
        data[0].pop(0)
        data[1].pop(0)
    return data
                

resolution = 1000.0
start_time = 0.0

def get_time():
    global start_time
    return get_raw_time() - start_time

def get_raw_time():
    global resolution
    return (round(time.time() * resolution) / resolution)

def reset_time():
    global start_time
    start_time = get_raw_time()

current_file = ""

def get_new_file(fileDir, name, ext):
    global current_file
    if len(name) == 0:
        return current_file
    if len(fileDir) > 0:
        fileDir += "/"
    filename = fileDir + name + "." + ext
    n = 1
    while os.path.isfile(filename):
        n += 1
        filename = fileDir + name + "-" + str(n) + "." + ext
    current_file = filename
    return filename

def write(words):
    global current_file
    if len(current_file) == 0:
        return
    with open(current_file, "a") as f:
        f.write(words + "\n")

def angle_avg(a, b):
  a -= 128
  b -= 128
  sum_angle = ((b - a + 128) % 256 - 128) / 2
  sum_angle = (a + sum_angle + 128) % 256 - 128
  return (sum_angle + 128) 

def average_angle_set(items):
    if len(items) > 0:
        if not (math.log2(len(items)) % 1.0 == 0):
            return -1.0
    else: return -1.0
    arr = []
    tempList = items.copy()
    while len(tempList) > 1:
        arr.append(angle_avg(tempList[0], tempList[1]))
        tempList.pop(0)
        tempList.pop(0)
    if len(arr) == 1:
        return arr[0]   
    return average_angle_set(arr)

def rolling_angle_filter(xData, yData, depth_exp):
    depth = 2**depth_exp
    if len(yData) < depth:
        return (xData, yData)
    xBuffer = []
    yBuffer = []
    for i in range(len(yData)-depth):
        xBuffer.append(xData[i])
        yBuffer.append(average_angle_set(yData[i:i+depth]))
    return (xBuffer, yBuffer)


def apply_strain_calculations(xdata, ydata, angle_depth=4, scale=1.0, isFlipped=True, rolling_depth=400, intercept=0.0):
  (xdata, ydata) = rolling_angle_filter(xdata, ydata, angle_depth)
  (xdata, ydata) = basic_rollover_fix(xdata, ydata, c=128) # 128 is standard
  extraYData = apply_rolling_filter(ydata.copy(), 1500)
  if rolling_depth > 0:
    ydata = apply_rolling_filter(ydata, rolling_depth)

  if isFlipped:
    for i in range(len(ydata)):
      ydata[i] *= -1
      extraYData[i] *= -1

  min1 = min(ydata)
  min2 = min(extraYData)
  time = xdata[0]

  for i in range(len(ydata)):
    ydata[i] -= min1
    extraYData[i] -= min2
    if is_number(scale):
        ydata[i] *= scale
        extraYData[i] *= scale
    else:
        ydata[i] = scale(ydata[i])
        extraYData[i] = scale(extraYData[i])
    xdata[i] -= time
    ydata[i] -= intercept
    extraYData[i] -= intercept

  return (xdata, ydata, extraYData)

# hugh's function
# post rollover function
def find_max_diff(ydata):
    diff_list = []
    for i in range(0, len(ydata)-1):
        diff_list.append(abs(ydata[i+1]-ydata[i]))
    return max(diff_list)