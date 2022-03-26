import tkinter as tk
from tkinter import IntVar
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
import valueFrame
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
   
options_row1_frame = valueFrame.valueFrame()
options_row2_frame = valueFrame.valueFrame()
options_row3_frame = valueFrame.valueFrame()
notes_frame = simpleUI.Frame()
time_frame = simpleUI.Frame()
options_button_frame = simpleUI.Frame()
text_field_frame = simpleUI.Frame()
button_frame = simpleUI.Frame()
text_frame = simpleUI.Frame()
collecting_label = -1
engine_plot = None

option1 = 69
option2 = 69
option3 = 69
option4 = 69
option5 = IntVar()
option6 = 69
options_text_indices = []
options_label_indices = []

notes = ""
time = ""
notes_text = ""
time_num = ""

def update_options():
    global option1, option2, option3, option4, option5, option6
    option1 = options_row1_frame.get_text(options_text_indices[0])
    option2 = options_row1_frame.get_text(options_text_indices[1])
    option3 = options_row2_frame.get_text(options_text_indices[2])
    option4 = options_row2_frame.get_text(options_text_indices[3])
    option6 = options_row3_frame.get_text(options_text_indices[5])
        
    options_row1_frame.update_label(options_label_indices[0], "Current Value: " + str(option1) + '\t')
    options_row1_frame.update_label(options_label_indices[1], "Current Value: " + str(option2) + '\t')
    options_row2_frame.update_label(options_label_indices[2], "Current Value: " + str(option3) + '\t')
    options_row2_frame.update_label(options_label_indices[3], "Current Value: " + str(option4) + '\t')
    options_row3_frame.update_label(options_label_indices[4], "   Current? " + ('True' if option5.get() == 1 else 'False') + '\t    ')
    options_row3_frame.update_label(options_label_indices[5], "Current Value: " + str(option6) + '\t')

def save_notes_and_time():
    notes_text = notes_frame.get_text(notes)
    time_num = time_frame.get_text(time)
    
    print(notes_text)
    print(time_num)
    
def update_running_label():
    global collecting, text_frame, collecting_label
    text_frame.update_label(collecting_label, "Running: " + str(collecting))

def create_ui(title):
    global text_field_frame, button_frame, text_frame, collecting_label, notes, time,\
           option1, option2, option3, option4, option5, option6
    simpleUI.set_title(title)
    
    temp1, temp2 = options_row1_frame.add_options("Option 1", 1, 25, True, option1, "Option 2", 1, 25, True, option2)
    options_text_indices.extend(temp1)
    options_label_indices.extend(temp2)
    temp1, temp2 = options_row2_frame.add_options("Option 3", 1, 25, True, option3, "Option 4", 1, 25, True, option4)
    options_text_indices.extend(temp1)
    options_label_indices.extend(temp2)
    temp1, temp2 = options_row3_frame.add_options("Option 5", 1, 25, False, option5, "Option 6", 1, 25, True, option6)
    options_text_indices.extend(temp1)
    options_label_indices.extend(temp2)
    options_button_frame.add_button("Update", 25, 1, "white", update_options, tk.LEFT)
    
    notes_frame.add_label("Notes:", 1, 25, tk.TOP)
    notes = notes_frame.add_text_box(5, 100, tk.BOTTOM)
    
    button_frame.create_cat_jam(label_side=tk.LEFT, label_anchor=tk.SW, flipped=True)
    button_frame.add_button("Start", 25, 5, "green", start_btn, tk.LEFT)
    button_frame.create_cat_jam(label_side=tk.RIGHT, label_anchor=tk.SE)
    button_frame.add_button("Stop", 25, 5, "red", stop_btn, tk.RIGHT)
    

    
    #text_field_frame.add_label("New File Name: ", 1, 25, tk.LEFT)
    #path_field = text_field_frame.add_text_box(1, 25, tk.LEFT)
    #text_field_frame.add_label(" ", 1, 25, tk.LEFT)
    
    time_frame.add_button("Set", 5, 1, "gray", save_notes_and_time, tk.RIGHT)
    time = time_frame.add_text_box(1, 25, tk.RIGHT)
    time_frame.add_label("Time: ", 1, 25, tk.RIGHT)
    
    path_field = ""
    path_text = text_frame.add_label("", 1, 25, tk.TOP)
    def update_path_text():
        global run_num, file_name, EXT, data_dir
        run_num = 0
        #file_name = get_new_file(data_dir, text_field_frame.get_text(path_field), EXT)
        file_name = get_new_file(data_dir, path_field, EXT)
        text_frame.update_label(path_text, "Current File:  " + file_name)
    update_path_text()

    #text_field_frame.add_button("Update", 5, 1, "gray", update_path_text, tk.RIGHT)

    collecting_label = text_frame.add_label("", 1, 25, tk.TOP)
    update_running_label()
    text_frame.add_label("", 1, 25, tk.TOP)
    
    #simpleUI.pack_first_in_window() # for cat jam jiff
    simpleUI.add_frame(options_row1_frame)
    simpleUI.add_frame(options_row2_frame)
    simpleUI.add_frame(options_row3_frame)
    simpleUI.add_frame(options_button_frame)
    simpleUI.add_frame(notes_frame)
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
