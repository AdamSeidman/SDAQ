import tkinter as tk
import sys
from fileUI import ClutchesFileUI
from dataUI import ClutchesDataUI
import random
from runhelpers import FileInfo
########################################

'''
Feel free to edit these variables.

default_test_name: original file name to write to
filter_depth: sets the rolling average filter depth
tpr: (ticks per revolution)
data_dir: directory for ct data
'''

filter_depth = 3
engine_tpr = 1.0

########################################

sys.path.append('/home/sdaq/Scripts/lib')
import sdaq
import graphing
import simpleUI
from valueFrame import ValueFrame, CheckFrame
from tools import *
import ctWriter as CT

dir_name = get_directory()
buffer = []
collecting = False
run_num = 1
def start_btn():
    global collecting, buffer
    if collecting == True:
        return
    collecting = True
    reset_time()
    buffer = []
    dataUI.update_running_label(collecting)

def stop_btn():
    global collecting, buffer, run_num, xData, yData, filter_depth, engine_tpr
    if collecting == False:
        return
    collecting = False
    dataUI.update_running_label(collecting)

def prepare_data():
    global buffer, engine_tpr, filter_depth
    (xData, yData) = convert_ticks_to_rpm(buffer, engine_tpr)
    yData = apply_rolling_filter(yData, filter_depth)
    yData[0] = 0
    return (xData, yData)

def prepare_false_data():
    xData = list()
    range_int = 10
    for i in range(range_int):
        xData.append(i)
    yData = list()
    for i in range(range_int):
        yData.append(random.randint(3, 10))
    return (xData, yData)

def update_time(time):
    global collecting
    if collecting:
        return
    try:
        time = float(str(time))
    except:
        return # todo popup invalid input
    #set_title
    (xData, yData) = prepare_data()
    update_plots(xData, yData)

def collect():
    global collecting, buffer
    if collecting:
        try:
            data = sdaq.get_i2c_data(0x08, [8])
            buffer.append((data, get_time()))
        except:
            pass

rpm_plot = None
last_rpm_plot = None

lastX = []
lastY = []
def update_plots(xData, yData):
    global lastX, lastY, rpm_plot, last_rpm_plot, run_num
    print ("Before plots")
    rpm_plot.plot(0, xData, yData)
    last_rpm_plot.plot(0, lastX, lastY)
    rpm_plot.set_title('Engine RPM Over Time: Run {}'.format(run_num))
    lastX = xData.copy()
    lastY = yData.copy()

clutches_options = [("Primary_Weight", "g"), ("Ramp", ""), ("Spring", "lb*in"), ("Helix", ""), ("Preload", "")]
clutches_checks = [("Modified_Belt-", True)]

fileUI = None
dataUI = None
def create_ui(title):
    global fileUI, dataUI, text_field_frame, button_frame, text_frame, collecting_label, notes, time, \
           clutches_options, clutches_checks, run_num, dir_name
    simpleUI.set_title(title)

    def file_update(frames, notes, update_frame, path_text):
        global run_num
        builder = ""
        for frame in frames:
            builder += frame.get_value()
        run_num = 0
        the_file = CT.start_new_file(dir_name, builder, notes)
        update_frame.update_label(path_text, "Current File:  " + the_file)
        file_info = FileInfo(dir_name, the_file)
        run_num = len(file_info.get_runs())

    
    fileUI = ClutchesFileUI(file_update, clutches_options, clutches_checks)
    simpleUI.add_frame(fileUI, tk.TOP)
    
    dataUI = ClutchesDataUI(start_btn, stop_btn, update_time)
    simpleUI.add_frame(dataUI, tk.BOTTOM)
    
    simpleUI.add_main_event(collect)
    simpleUI.start_window()

def main():
    global rpm_plot, last_rpm_plot
    rpm_plot = graphing.Plot(title='Engine RPM Over Time: Run #1', xlabel='Seconds', ylabel='RPM')
    last_rpm_plot = graphing.Plot(title='Last Engine RPM Over Time', xlabel='Seconds', ylabel='RPM', line_type=".r-") # todo check line type
    sdaq.create_i2c_bus()
    create_ui('RPM Data Collector')

if __name__ == "__main__":
    main()
