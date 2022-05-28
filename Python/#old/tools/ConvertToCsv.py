import ast
import argparse
parser = argparse.ArgumentParser(description="Process data from .sdaq into .csv")
parser.add_argument('inFile', metavar='inFile', type=str, help="A .sdaq file to process")
parser.add_argument('outFile', metavar='outFile', type=str, help="A .csv file to output")
args = parser.parse_args()
inFile = args.inFile
class SensorDump:
        def __init__(self, time: float, arr: list):
            self.time = time
            self.arr = arr
            self.sensorid = arr[0]
            arr.pop(0)
        def to_csv_row(self):
            string = ""
            string = string + str(self.time) + ','
            string = string + str(self.sensorid) + ','
            for i in range(len(self.arr)):
                string = string + str(self.arr[i])
                if i != len(self.arr)-1:
                    string = string + ','
            return string
outgest_var = list()
f = open(inFile)
my_strs = f.readlines()
total_string = str()
longest_ingest = 0
for my_str in my_strs:
    ingest_var = ast.literal_eval(my_str)
    for i in range(0, len(ingest_var), 2):
        dump = SensorDump(ingest_var[i], ingest_var[i + 1])
        longest_ingest = max(longest_ingest, len(dump.arr))
        total_string = total_string + '\n' + dump.to_csv_row()
outF = open(args.outFile, "w")
titleString = "Time, Address,"
for i in range(longest_ingest):
    titleString = titleString + " Sensor{}".format(i)
    if i != longest_ingest - 1:
        titleString = titleString + ','
outF.write(titleString)
outF.write(total_string)
f.close()
outF.close()