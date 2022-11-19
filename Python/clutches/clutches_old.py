import tkinter as tk
import sys
from clutchesUI import ClutchesUI
import random

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

sys.path.append(os.path.abspath('../../lib'))

import sdaq
import graphing
import simpleUI
from valueFrame import ValueFrame, CheckFrame
from tools import *
import ctWriter as CT

restart_num = True
# All globals up here
dir_name = None

while dir_name is None:
    dir_name = get_directory()
    if get_num_of_files(dir_name) > 0:
        num = simpleUI.create_type_popup(popup_msg="Warning: The selected directory has files already in it.\nWould you like to continue?")
        if num is False:
            dir_name = None
        else:
            CT.set_setup_num(get_num_of_files(dir_name) + 1)

buffer = []
collecting = False
has_written = False

ui = None
rpm_plot = None

clutches_options = [("Primary_Weight", "g"), ("Ramp", ""), ("Spring", "lb*in"), ("Helix", ""), ("Preload", "")]
clutches_checks = [("Modified_Belt-", True)]

def start_btn():
    global collecting, buffer, has_written
    if collecting == True:
        return
    collecting = True
    has_written = False
    reset_time()
    buffer = []
    ui.update_running_label(collecting)

def stop_btn():
    global collecting, buffer, run_num, xData, yData, filter_depth, engine_tpr
    if collecting == False:
        return
    collecting = False
    ui.update_running_label(collecting)

def prepare_data():
    global buffer, engine_tpr, filter_depth
    (xData, yData) = convert_ticks_to_rpm(buffer, engine_tpr)
    yData = apply_rolling_filter(yData, filter_depth)
    xData, yData = shift_around_val([[xData, yData]], 2150, extra=1)[0]
    xData, yData = apply_cutoff([xData, yData], 0)
    xData[0] = 0
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
    global collecting, has_written
    if collecting or has_written:
        if collecting:
            simpleUI.create_type_popup(popup_msg="Please stop the time collection before trying to write the time")
        else:
            simpleUI.create_type_popup(popup_msg="You have already set the time for this run")
        return
    try:
        time = float(str(time))
    except:
        simpleUI.create_type_popup(popup_msg="You need to input an actual time")
        return
    has_written = True
    #set_title
    (xData, yData) = prepare_data() # todo
    update_plots(xData, yData)
    CT.write_data(xData, yData, time)

def update_plots(xData, yData):
    # todo MORE
    global rpm_plot
    rpm_plot.update_title("Engine RPM Over Time: Run #{}".format(CT.get_run_num()))
    rpm_plot.plot(0, xData, yData)


def update_file(path_text, notes):
    global dir_name
    if CT.has_setup(path_text):
        simpleUI.create_popup(popup_msg="You've already used this setup, you can continue if you want.")
    return CT.start_new_file(dir_name, path_text, notes)

def collect():
    global collecting, buffer
    if collecting:
        try:
            data = sdaq.get_i2c_data(0x08, [5])
            buffer.append((data, get_time()))
        except:
            pass

def create_ui(title):
    global ui, clutches_options, clutches_checks
    ui = ClutchesUI(title, clutches_options, clutches_checks, startFn=start_btn, stopFn=stop_btn, fileUpdateFn=update_file, timeSetFn=update_time)
    ui.start_main_event(collect)

def main():
    global rpm_plot, ui
    rpm_plot = graphing.Plot(title='Engine RPM Over Time: Run #1', xlabel='Seconds', ylabel='RPM')
    sdaq.create_i2c_bus()    
    create_ui('RPM Data Collector')

if __name__ == "__main__":
    main()
