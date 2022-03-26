import time
import os.path

def convert_ticks_to_rpm(ticks, tpr):
    xData = [0]
    yData = [0]
    lastTickTime = -1000.0;
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

def apply_rollover_fix(data):
    if len(data) <= 2:
        return data
    lastVal = data[0]
    for i in range(1, len(data)):
        ndiff = abs(lastVal - (data[i] - 255))
        diff = abs(lastVal - data[i])
        pdiff = abs(lastVal - (data[i] + 255))
        dmin = min(ndiff, diff, pdiff)
        if abs(dmin - diff) > 75:
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

def shift_around_val(data, val):
    for index in range(len(data)):
        ydata = data[index][1]
        num = 0
        for i in range(len(ydata)):
            if ydata[i] >= val:
                num = data[index][0][i]
                break
        xdata = []
        for i in range(len(ydata)):
            xdata.append((data[index][0][i]) - num)
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