import sys

# Writer of .ct (Clutch Tuning)

sys.path.append('/home/sdaq/Scripts/lib')
from tools import *

EXT = "ct"

has_written = False
run_num = 1
file_name = ""
notes = ""
setup_num = 0
prelim_filename = ""

def set_setup_num(num):
    global setup_num
    # set to number of files + 0
    setup_num = num

def start_new_file(dir_name, filename, file_notes):
    global, run_num, file_name, notes, has_written, setup_num, EXT, prelim_filename
    setup_num += 1
    has_written = False
    prelim_filename = filename
    run_num = 1
    file_name = get_new_file(dir_name, str(setupNum) + "_" + filename, EXT)
    notes = file_notes

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

def write_data(xData, yData, time):
    global has_written, prelim_filename, notes, run_num
    if not has_written:
        has_written = True
        write(str(prelim_filename))
        write(str(notes))
    write("\nRun #" + str(run_num) + ": " + str(time) + " s")
    write(str(xData))
    write(str(yData))
    run_num += 1