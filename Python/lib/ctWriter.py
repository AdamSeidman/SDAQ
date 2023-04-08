import sys

# Writer of .ct (Clutch Tuning)

import os
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "..", "lib")
path = os.path.abspath(path)
sys.path.append(path)
from tools import *

EXT = "ct"

has_written = False
dir_name = ""
run_num = 1
file_name = ""
notes = ""
setup_num = 1
prelim_filename = ""
name_buffer = []

def set_setup_num(num):
    global setup_num
    # set to number of files + 1
    setup_num = num + 1

def start_new_file(dirname, filename, file_notes):
    global run_num, dir_name, file_name, notes, has_written, setup_num, EXT, prelim_filename
    if has_written:
        setup_num += 1
        has_written = False
    prelim_filename = filename
    dir_name = dirname
    run_num = 1
    file_name = get_new_file(dirname, str(setup_num) + "_" + filename, EXT)
    notes = file_notes
    return file_name

def get_setup_num():
    global setup_num
    return setup_num

def get_file_name():
    global file_name
    return file_name

def get_run_num():
    global run_num
    return run_num

def get_notes():
    global notes
    return notes

def has_setup(setup_name):
    global name_buffer
    return setup_name in name_buffer

def write_data(xData: "list[int] | list[list[int]]", yData, time):
    global has_written, prelim_filename, notes, run_num, name_buffer
    if len(prelim_filename) == 0:
        pass #popup saying update hasnt been pressed yet
    if not has_written:
        has_written = True
        write(str(prelim_filename))
        name_buffer.append(str(prelim_filename))
        write("Notes:\n")
        write(str(notes))
    write("\nRun #" + str(run_num) + ": " + str(time) + " s")
    write(str(xData))
    write(str(yData))
    run_num += 1

def write_multidata(xData, yDataList, time):
    """
    For fun fact: the format of this turns out to be very similar to the above write_data, allowing us to discern based on the number of [] the actual file format at the time...
    """
    global has_written, prelim_filename, notes, run_num, name_buffer
    if len(prelim_filename) == 0:
        pass #popup saying update hasnt been pressed yet
    if not has_written:
        has_written = True
        write(str(prelim_filename))
        name_buffer.append(str(prelim_filename))
        write("Notes:\n")
        write(str(notes))
    write("\nRun #" + str(run_num) + ": " + str(time) + " s")
    write(str(xData))
    for item in yDataList:
        write(str(item))
    run_num += 1