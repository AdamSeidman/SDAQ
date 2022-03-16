import tkinter as tk
import sys

########################################

'''
Feel free to edit these variables.

default_test_name: original file name to write to
filter_depth: sets the rolling average filter depth
tpr: (ticks per revolution)
data_dir: directory for ct data
'''

default_test_name = "clutch-testing"
filter_depth = 3
engine_tpr = 1.0
data_dir = "./data"

########################################

sys.path.append('/home/sdaq/Scripts/lib')
import sdaq
import graphing
import simpleUI
from tools import *

buffer = []
collecting = False
run_num = 1
EXT = 'ct'
file_name = get_new_file(data_dir, default_test_name, EXT)

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
        
text_field_frame = simpleUI.Frame()
button_frame = simpleUI.Frame()
text_frame = simpleUI.Frame()
collecting_label = -1
engine_plot = None

def update_running_label():
    global collecting, text_frame, collecting_label
    text_frame.update_label(collecting_label, "Running: " + str(collecting))

def create_ui(title):
    global text_field_frame, button_frame, text_frame, collecting_label
    simpleUI.set_title(title)
    
    button_frame.add_button("Start", 25, 5, "green", start_btn, tk.LEFT)
    button_frame.add_button("Stop", 25, 5, "red", stop_btn, tk.RIGHT)
    
    text_field_frame.add_label("New File Name: ", 1, 25, tk.LEFT)
    path_field = text_field_frame.add_text_box(1, 25, tk.LEFT)
    text_field_frame.add_label(" ", 1, 25, tk.LEFT)

    path_text = text_frame.add_label("", 1, 25, tk.TOP)
    def update_path_text():
        global run_num, file_name, EXT, data_dir
        run_num = 0
        file_name = get_new_file(data_dir, text_field_frame.get_text(path_field), EXT)
        text_frame.update_label(path_text, "Current File:  " + file_name)
    update_path_text()

    text_field_frame.add_button("Update", 5, 1, "gray", update_path_text, tk.RIGHT)

    collecting_label = text_frame.add_label("", 1, 25, tk.TOP)
    update_running_label()
    text_frame.add_label("", 1, 25, tk.TOP)

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
