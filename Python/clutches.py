import tkinter as tk
from tkinter import IntVar
import sys
from fileUI import ClutchesFileUI

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

def start_new_file(test_name, notes, beginning=False):
    global EXT
    file_name = get_new_file(dir_name, test_name, EXT)
    if not beginning:
        write(test_name + "\n")
        write(notes)
    return file_name

def write_to_file(xData, yData):
    global run_num
    write("\nRun " + str(run_num + 1) + ":")
    write(str(xData))
    write(str(yData))

def start_btn():
    global collecting, buffer
    if collecting == True:
        return
    collecting = True
    reset_time()
    buffer = []
    update_running_label()

def stop_btn():
    global collecting, buffer, run_num, xData, yData, filter_depth, engine_tpr
    if collecting == False:
        return
    collecting = False
    (xData, yData) = convert_ticks_to_rpm(buffer, engine_tpr)
    yData = apply_rolling_filter(yData, filter_depth)
    yData[0] = 0
    write_to_file(xData, yData)
    run_num += 1
    engine_plot.plot(0, xData, yData)
    engine_plot.set_title('Engine RPM Over Time: Run #' + str(run_num))
    update_running_label()

def collect():
    global collecting, buffer
    if collecting:
        try:
            data = sdaq.get_i2c_data(0x08, [8])
            buffer.append((data, get_time()))
        except:
            pass

fileUI = None

time_frame = simpleUI.Frame()
text_field_frame = simpleUI.Frame()
text_frame = simpleUI.Frame()
button_frame = simpleUI.Frame()

collecting_label = -1
engine_plot = None

time = ""
time_num = ""
    
def update_running_label():
    global collecting, text_frame, collecting_label
    text_frame.update_label(collecting_label, "Running: " + str(collecting))

clutches_options = [("Primary_Weight", "g"), ("Ramp", ""), ("Spring", "lb*in"), ("Helix", ""), ("Preload", "")]
clutches_checks = [("Modified_Belt-", True)]

def create_ui(title):
    global fileUI, text_field_frame, button_frame, text_frame, collecting_label, notes, time, \
           clutches_options, clutches_checks, run_num
    
    simpleUI.set_title(title)
    
    def file_update(frames, notes, update_frame, path_text, begin_file):
        builder = ""
        for frame in frames:
            builder += frame.get_value()
        run_num = 0
        update_frame.update_label(path_text, "Current File:  " + start_new_file(builder, notes, beginning=begin_file))
    
    fileUI = ClutchesFileUI(file_update, clutches_options, clutches_checks)
    simpleUI.add_frame(fileUI, tk.TOP)
    
    button_frame.create_cat_jam(label_side=tk.LEFT, label_anchor=tk.SW, flipped=True)
    button_frame.add_button("Start", 25, 5, "green", start_btn, tk.LEFT)
    button_frame.create_cat_jam(label_side=tk.RIGHT, label_anchor=tk.SE)
    button_frame.add_button("Stop", 25, 5, "red", stop_btn, tk.RIGHT)
    
    time_frame.add_label(" ", tk.TOP) # spacer
    time_frame.add_button("Set", 5, 1, "lightgray", lambda: print("Time Set"), tk.RIGHT)
    time = time_frame.add_text_box(1, 25, tk.RIGHT)
    time_frame.add_label("Time: ", tk.RIGHT)

    collecting_label = text_frame.add_label("", tk.TOP)
    update_running_label()
    text_frame.add_label(" ", tk.TOP)
    
    simpleUI.add_frame(time_frame)
    simpleUI.add_frame(text_field_frame)
    simpleUI.add_frame(text_frame)
    simpleUI.add_frame(button_frame, window_side=tk.BOTTOM)
    
    simpleUI.add_main_event(collect)
    simpleUI.start_window()

def main():
    global engine_plot
    engine_plot = graphing.Plot(title='Engine RPM Over Time: Run #1', xlabel='Seconds', ylabel='RPM')
    sdaq.create_i2c_bus()
    create_ui('RPM Data Collector')

if __name__ == "__main__":
    main()
