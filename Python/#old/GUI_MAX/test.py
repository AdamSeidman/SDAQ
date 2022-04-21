import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from configparser import ConfigParser

config = ConfigParser()
root = Tk()

# Create a new file if it doesn't exist
# f1 = open("configs/config1.ini", "w")

# Read from config file and write into it
# config.read('configs/config.ini')
# adds sections to new configs
# config.add_section('')
# config.set('calibration', 'key1', 'value1')
# config.set('calibration', 'key2', 'value2')
# config.set('calibration', 'key3', 'value3')

# with open('configs/config.ini', 'w') as f:
#     config.write(f)


# Read from config file and read based on sections
config.read('GUI/configs/config.ini')

print(config.get('calibration', 'key1'))  # -> "value1"
print(config.get('calibration', 'key2'))  # -> "value2"
print(config.get('calibration', 'key3'))  # -> "value3"
print(config.get('calibration', 'key4'))
print(config.get('calibration', 'key5'))

board_selected = config.get('boards', 'board_1').split(',')
print(board_selected[0])
print(config.get('boards', 'board_1'))

print(config.get('sensors', 'sensor_name_1'))
print(config.get('sensors', 'sensor_slots_1'))

file_path_entry = tkinter.StringVar()
current_value = tkinter.StringVar()


def save():
    file_path = file_path_entry.get()

    if len(file_path) == 0:
        Files = [('All Files', '*.*'),
                 ('Python Files', '*.py'),
                 ('Text Document', '*.txt')]
        file_path = filedialog.asksaveasfilename(filetypes=Files, defaultextension=Files)

    try:
        with open(file_path, "w") as file:
            config.write(file)
        return "saved"

    except FileNotFoundError:
        return "File Not Found!"


# updates value for another element to display
def return_entry(scaleNum):
    resultLabel.config(text=round(float(scaleNum), 2))
    scaleScum = scaleNum[0:5]
    current_value.set(scaleScum)


# updates Scale(Slider) value to spinbox value
def set_scale():
    scaleNum = spinbox.get()
    scale.set(scaleNum)


# GUI basics
root.title("Testing GUI Elements")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Testing").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Save", command=save).grid(column=0, row=1)
ttk.Entry(root, textvariable=file_path_entry, font=('comic-sans', 10, 'normal')).grid(column=0, row=1)
ttk.Scale(root, from_=0, to=42, orient=VERTICAL).grid(column=0, row=2)
# Separate grid and GUI interactive element to allow manipulation of it
scale = ttk.Scale(root, from_=0, to=70, orient=HORIZONTAL, command=return_entry)
scale.grid(column=1, row=1)
resultLabel = Label(root, text = "")
resultLabel.grid(column=3, row=3)
spinbox = ttk.Spinbox(root, textvariable=current_value, from_=0, to=70, command=set_scale)
spinbox.grid(column=2, row=2)
root.mainloop()

