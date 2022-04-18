import time
import os.path

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
        if abs(buffer[i]) > 5:
            indexes.append(i)
    newXData = []
    newYData = []
    newBuffer = []
    for i in range(len(buffer)):
        if i not in indexes:
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