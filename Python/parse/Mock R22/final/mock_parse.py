import os.path
import sys

sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")
#import graphing
from tools import *

filename = "DockDrop3"
ext="sdaq"
dirname = "C:/Users/Adam/Documents/#Code/SDAQ/Data/4_20_Frame_and_Brakes"
num = 0

newfile = dirname + "/" + "raw_dock_drop_3.csv"
num_sensors = 2 # 5 or 6

file = None

nums = [1]

def get_next_file():
    global filename, ext, dirname, num
    numStr = ""
    if num >= 2:
        numStr = "-" + str(num)
    return (dirname + "/" + filename + numStr + "." + ext)

def getFile():
    global file, num
    if file is None:
        num = 1
    else:
        num += 1
    file = get_next_file()
    if not os.path.isfile(file):
        file = None
        return False
    return True

getFile()

data = [[0.0, 0]]
writeImm = True

def main():
    global newfile, num_sensors, file, nums, data, writeImm
    count = 0
    print("Starting")
    wf = open(newfile, "w")
    startNum = 0
    bgng = False
    while not (file is None):
        print(file)
        f = open(file, "r")
        #yeet = False
        for line in f:
            if len(line) < 5:
                continue
            items = line.replace("[", "").replace("]", "").replace(",", "").replace("  ", " ").split()
            for item in items:
                if count == 0:
                    #if asdsfghjkl
                    if not bgng:
                        bgng = True
                    elif writeImm:
                        wf.write("\n")
                    
                    if startNum == 0:
                        print(item)
                        startNum = float(item) - 10
                    
                    time = float(float(item) - startNum) / 1000.0

                    if writeImm:
                        wf.write(str(time))
                        wf.write(",")
                    else:
                        data.append([time])
                elif count in nums:
                    #if (count == 1) and not (item == "255"):
                        #print("fdf")
                    if writeImm:
                        wf.write(item)
                        wf.write(",")
                    else:
                        (data[len(data) - 1]).append(int(item))

                count = (count + 1) % (num_sensors + 1)
            if writeImm:
                wf.write("\n")
            count = 0
        f.close()
        getFile()
    if not writeImm:
        (xData, yData) = convert_ticks_to_rpm(data, 1.0)
        for i in range(len(xData)):
            wf.write(str(xData[i]))
            wf.write(",")
            wf.write(str(yData[i]))
            wf.write(",\n")
    wf.close()

if __name__ == "__main__":
    main()