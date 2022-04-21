import time
import os.path
from tkinter.filedialog import askdirectory
import math

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
    try:
        check = int(num)
        flag = True
    except ValueError:
        flag = False
    
    return flag


def convert_ticks_to_rpm(ticks, tpr):
    xData = [0]
    yData = [0]
    lastTickTime = -1000.0
    lastTick = 0
    for tick in ticks:
        if not (tick[0] == lastTick) and ((tick[0] == 255) or (tick[0] == 1)):
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

# original rollover fic algorithm
def apply_rollover_fix(data, c=75):
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

# test function for original algorithm
def apply_rollover_fix_test(data, c=75):
    if len(data) <= 2:
        return data
    for i in range(1, len(data)):
        lastVal = data[i-1]
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

#def filter_outliers(xdata, ydata):

# 2nd attempt at buffer algorithm
# uses outlier data filter
def funny2(xdata, ydata):
    if len(ydata) <= 2:
        return ydata
    buffer = []
    for i in range(1, len(ydata)):
        prev = ydata[i-1]
        curr = ydata[i]
        a = prev - (curr + 256)
        b = prev - (curr)
        c = prev - (curr - 256)
        dmin = min(abs(a), abs(b), abs(c))
        if abs(a) == dmin:
            buffer.append(a)
        elif abs(b) == dmin:
            buffer.append(b)
        else:
            buffer.append(c)
    #result = [ydata[1]]
    buffer.insert(0, 0)
    indexes = []
    for i in range(0, len(buffer)):
        # outlier filter, change inequality
        # lower value = more filtered
        if abs(buffer[i]) > 30:
            indexes.append(i)
    newXData = []
    newYData = []
    newBuffer = []
    for i in range(len(buffer)):
        if i not in indexes and (i-1) not in indexes and (i+1) not in indexes:
            newXData.append(xdata[i])
            newYData.append(ydata[i])
            newBuffer.append(buffer[i])
    results = [ydata[0]]
    #for i in range(1,len(buffer)):
    #    results
    #print(buffer)
    for i in range(1, len(newBuffer)):
        results.append(results[len(results) - 1] + newBuffer[i])
    return (newXData, results)

# algorithm using buffer to apply to data
def funny(data):
    if len(data) <= 2:
        return data
    buffer = []
    for i in range(1, len(data)):
        prev = data[i-1]
        curr = data[i]
        a = prev - (curr + 256)
        b = prev - (curr)
        c = prev - (curr - 256)
        dmin = min(abs(a), abs(b), abs(c))
        if abs(a) == dmin:
            buffer.append(a)
        elif abs(b) == dmin:
            buffer.append(b)
        else:
            buffer.append(c)
        if buffer[len(buffer) - 2] == -121.0 and buffer[len(buffer) - 1] == 112.0:
            for j in range(i - 3, i + 3):
                print(data[j])
    result = [data[1]]
    #print(buffer)
    for i in range(0, len(buffer)):
        result.append(result[len(result)-1] + buffer[i]) #replaced last two result with data
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
    f = open(current_file, "a")
    f.write(words + "\n")
    f.close()

# This works
def angle_avg(a, b):
  a -= 128
  b -= 128
  sum_angle = ((b - a + 128) % 256 - 128) / 2
  sum_angle = (a + sum_angle + 128) % 256 - 128
  return (sum_angle + 128) 

# This works
def angle_avg_set(items):
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
    return angle_avg_set(arr)

# This works
def rolling_angle_filter(data, depth_exp, c=64):
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
    return data

# This probably has a very long computation time
# See the normal tools.apply_rolling_filter for reference
def rolling_angle_filter2(data, depth_exp):
  depth = 2**depth_exp # only allow the depth to be a power of 2
  if len(data) < depth:
    depth = len(data)
  buffer = data[0:depth]
  for i in range(len(data)):
    buffer[i % depth] = data[i]
    # the following line should be the only different one
    # its just getting the average using our own function instead
    data[i] = angle_avg_set(buffer.copy()) # this comes from prev message
  return data

def rolling_angle_filter3(xData, data, depth_exp):
    depth = 2**depth_exp
    if len(data) < depth:
        return data
    newData = []
    for i in range(depth, len(data) - 1):
        buffer = data[i:depth].copy()
        newData.append(angle_avg_set(buffer))
    while len(xData) > len(data):
        xData.pop(0)
    return (xData, data)

def angle_avg_A(a, b): # somewhat copied from stack overflow...
  a -= 128
  b -= 128
  sum_angle = ((b - a + 128) % 256 - 128) / 2
  sum_angle = (a + sum_angle + 128) % 256 - 128
  return (sum_angle + 128) 

def angle_avg_set_A(items):
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

def rolling_angle_filter_A(xData, data, depth_exp):
    depth = 2**depth_exp
    if len(data) < depth: # don't bother with short data
        return data
    newData = [] # new array for averaged data
    for i in range(depth, len(data) - 1):
        buffer = data[i-depth:i].copy() # get depth-length slice of data
        newData.append(angle_avg_set_A(buffer))
    while len(xData) > len(data):
        xData.pop(0) # make them the same length (x and y)
    return (xData, data)

# hugh's function
# post rollover function
def find_max_diff(ydata):
    diff_list = []
    for i in range(0, len(ydata)-1):
        diff_list.append(abs(ydata[i+1]-ydata[i]))
    return max(diff_list)