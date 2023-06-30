import tkinter as tk
import sys
from clutchesUI import ClutchesUI
import random
import os
import traceback
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

path = os.path.dirname(os.path.abspath(__file__))
path = path + "\\..\\lib"
path = os.path.abspath(path)
sys.path.append(path)

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

def prepare_data() -> "tuple[list[int], list[int]] | tuple[list[int], list[int], list[int]]":
    """
    Technically this can be applied to however many hall effect sensors we anticipate, I'm not going there at the moment however, so....
    """
    global buffer, engine_tpr, filter_depth
    engineData = []
    primaryData = []
    if len(buffer) == 0:
        return([], [])

    if type(buffer[0][0]) == list:
        engineData = [(x[0][0], x[1]) for x in buffer]
        if len(buffer[0][0]) > 1:
            # Explanation: x[0] is the "data" and x[1] is the "time"
            # If there's more than one piece of data it's therefore easier to just do this in order to split it
            primaryData = [(x[0][1], x[1]) for x in buffer]
    else:
        engineData = [(x[0], x[1]) for x in buffer]
    
    (engineDatax, engineDatay) = convert_ticks_to_rpm(engineData, engine_tpr)
    engineDatay = apply_rolling_filter(engineDatay, filter_depth)
    engineDatax, engineDatay = shift_around_val([[engineDatax, engineDatay]], 2150, extra=1)[0]
    engineDatax, engineDatay = apply_cutoff([engineDatax, engineDatay], 0)
    engineDatax[0] = 0
    engineDatay[0] = 0
    if len(primaryData) > 0:
        (primaryDatax, primaryDatay) = convert_ticks_to_rpm(primaryData, engine_tpr)
        primaryDatay = apply_rolling_filter(primaryDatay, filter_depth)
        primaryDatax, primaryDatay = shift_around_val([[primaryDatax, primaryDatay]], 2150, extra=1)[0]
        primaryDatax, primaryDatay = apply_cutoff([primaryDatax, primaryDatay], 0)
        primaryDatax[0] = 0
        primaryDatay[0] = 0
        # The x data is the exact same for both, we can abuse the hell out of this
        return (engineDatax, engineDatay, primaryDatay)
    # only return the data we need
    return (engineDatax, engineDatay)

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
    tup = prepare_data() # todo
    if (len(tup) == 2):
        update_plots(tup[0], tup[1])
        CT.write_data(tup[0], tup[1], time)
    else:
        update_multiplot(tup[0], [*tup[1:]])
        CT.write_multidata(tup[0], [*tup[1:]], time)

def update_plots(xData, yData):
    # todo MORE
    global rpm_plot
    rpm_plot.update_title("Engine RPM Over Time: Run #{}".format(CT.get_run_num()))
    rpm_plot.plot(0, xData, yData)

def update_multiplot(xData, yDataList):
    global rpm_plot
    assert type(rpm_plot) is graphing.Plot
    rpm_plot.update_title("Engine RPM Over Time: Run #{}".format(CT.get_run_num()))
    for i in range(len(yDataList)):
        rpm_plot.plot(i, xData, yDataList[i])

def update_file(path_text, notes):
    global dir_name
    if CT.has_setup(path_text):
        simpleUI.create_popup(popup_msg="You've already used this setup, you can continue if you want.")
    return CT.start_new_file(dir_name, path_text, notes)

def collect():
    global collecting, buffer
    if collecting:
        try:
            data = sdaq.get_i2c_data(0x08, [5, 6])
            buffer.append((data, get_time()))
        except Exception as e:
            print(traceback.format_exc())
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
