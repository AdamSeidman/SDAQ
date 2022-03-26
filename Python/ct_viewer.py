#import tkinter as tk
import sys
import os

#sys.path.append('Python\lib')
sys.path.append('/home/sdaq/Scripts/lib')
import graphing
#import simpleUI
import tools
#from tools import *

ext = 'ct'

from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
dirname = "/home/sdaq/Desktop/clutches/max_data/"
#dirname = askdirectory() # show an "Open" dialog box and return the path to the selected file

files = []

def update_files():
    global files, ext
    numChars = 1 + len(ext)
    for file in os.listdir(dirname):
        #print((file[-3]).lower())
        if len(file) > numChars:# and (file[-3]).lower() == ('.' + ext):
            files.append(file)

update_files()

def convert_to_num_array(str):
    str = str.split(',')
    buf = []
    for s in str:
        buf.append(float(s))
    return buf

def read_ct_file(filename):
    f = open("/home/sdaq/Desktop/clutches/max_data/" + filename, "r")
    print(filename)
    lines = []
    n = 0
    for x in f:
        if n > 1:
            lines.append(x.replace(" ", "").replace("[","").replace("]",""))
        n = (n + 1) % 4
        
    buf = []
    n = 0
    for i in range(int(len(lines) / 2)):
        buf.append([])
        buf[n].append(convert_to_num_array(lines[i * 2]))
        buf[n].append(convert_to_num_array(lines[(i * 2) + 1]))
        n += 1
    return buf

max_line_nums = 0

plot = graphing.Plot(line_type="", title="Clutches Test: Setup 5")

def create_averaged_plot(data):
    global plot
    #plot2 = graphing.Plot(".k-", title="Averaged")
    new_data = tools.combine_data(data)
    new_data = tools.apply_cutoff(new_data, -0.25)
    new_data[1] = tools.apply_rolling_filter(new_data[1], 3)
    new_data[1][0] = 0
    print(new_data)
    plot.plot(0, new_data[0], new_data[1])
    
def create_centered_plot(filename, center_val):
    global max_line_nums
    data = read_ct_file(filename)
    data = tools.shift_around_val(data, center_val)
    if max_line_nums >= len(data):
        for i in range(max_line_nums):
            plot.plot(i, [], [])
    max_line_nums = max(max_line_nums, len(data))
    n = 0
    for line in data:
        #plot.plot(n, line[0], line[1])
        n += 1
    create_averaged_plot(data)

if len(files) > 0:
    create_centered_plot('3_25_22_setup 5.ct', 2150) # todo check