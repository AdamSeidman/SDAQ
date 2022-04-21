from pathlib import Path
from os import walk

from configparser import ConfigParser
from tkinter import filedialog

# from tkinter import *
from tkinter import Tk, Canvas, Spinbox, Label, OptionMenu, StringVar, Button, PhotoImage

# Path to assets (buttons, live feed, etc)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("src/assets")

# Path to Tests
TESTS_PATH = OUTPUT_PATH / Path("src/tests")


# get the path to assets
def relative_to_path(path: str) -> Path:
    return ASSETS_PATH / Path(path)

file_path = ""


def save():
    if len(file_path) == 0:
        Files = [('All Files', '*.*'),
                 ('CSV Document', '*.csv'),
                 ('Text Document', '*.txt'),
                 ('Excel Workbook', '*.xlsx')]
        file_path = filedialog.asksaveasfilename(filetypes=Files, defaultextension=Files, initialdir = "GUI\configs")

    try:
        with open(file_path, 'w') as file:
            config.write(file)
        return "saved"

    except FileNotFoundError:
        return "File Not Found!"

def load():
    pass

# Create the Tkinter window, give name, and get the icon
window = Tk()
window.title("SDAQ")
window.iconbitmap(relative_to_path("sdaq.ico"))

# set window's color and size
window.geometry("1366x768")
window.configure(bg="#FFFFFF")

# Create canvas for background image)
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=768,
    width=1366,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Set Background image (can be any)
background_image = PhotoImage(
    file=relative_to_path("image_1.png"))
background = canvas.create_image(
    683,
    384,
    image=background_image
)

# Rectangle at the bottom
canvas.create_rectangle(
    8,
    733,
    1366,
    768,
    fill="#3B719F",
    outline="")


### LIVE FEED ######################################################

# Live Feed Output
live_feed = Label(
    bd=0,
    bg="#DFDFDF",
    highlightthickness=0
)
live_feed.place(
    x=985,
    y=176,
    width=315,
    height=454
)
canvas.create_text(
    985,
    156,
    anchor="nw",
    text="Live Feed",
    fill="#000000",
    font=("Roboto", 17 * -1)
)

# Button to start Live Feed
live_feed_start_image = PhotoImage(
    file=relative_to_path("button_1.png"))
live_feed_start_button = Button(
    image=live_feed_start_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("start live feed button clicked"),
    relief="flat"
)
live_feed_start_button.place(
    x=985,
    y=637,
    width=112,
    height=50
)

# Button to save collected data
live_feed_save_image = PhotoImage(
    file=relative_to_path("button_2.png"))
live_feed_save_button = Button(
    image=live_feed_save_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("save collected data button clicked"),
    relief="flat"
)
live_feed_save_button.place(
    x=1188,
    y=637,
    width=112,
    height=50
)

####################################################################

### Config Options #####################################################################

# Button to load configs
cfg_load_image = PhotoImage(
    file=relative_to_path("button_3.png"))
cfg_load_button = Button(
    image=cfg_load_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("load config button clicked"),
    relief="flat"
)
cfg_load_button.place(
    x=1214,
    y=87,
    width=86,
    height=20
)

# Button to save configs
cfg_save_image = PhotoImage(
    file=relative_to_path("button_4.png"))
cfg_save_button = Button(
    image=cfg_save_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save,
    relief="flat"
)
cfg_save_button.place(
    x=1104,
    y=87,
    width=86,
    height=20
)

canvas.create_text(
    1022,
    56,
    anchor="nw",
    text="Configuration Loaded:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
canvas.create_text(
    1214,
    56,
    anchor="nw",
    text="config1.cfg",
    fill="#000000",
    font=("Roboto", 17 * -1)
)

########################################################################################

### Board Description ##############################################################################

canvas.create_text(
    66,
    56,
    anchor="nw",
    text="Number Of Boards: ",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
canvas.create_text(
    235,
    56,
    anchor="nw",
    text="1",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
canvas.create_text(
    66,
    85,
    anchor="nw",
    text="Current Board:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)

# Board Options
brdvar = StringVar(canvas)
brdvar.set('board1')
choices = {'board1', 'board2', 'board3'}
cfg_options = OptionMenu(
    canvas,
    brdvar,
    *choices
)
cfg_options.place(
    x=185,
    y=82,
    width=110,
    height=25
)

####################################################################################################

### Tests ##########################################

# Button for tests (e.g. LED cycle)
test_button_image = PhotoImage(
    file=relative_to_path("button_5.png"))
test_button = Button(
    image=test_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("test button clicked"),
    relief="flat"
)
test_button.place(
    x=858,
    y=87,
    width=86,
    height=20
)

# Test Options
canvas.create_text(
    790,
    56,
    anchor="nw",
    text="Test:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
filenames = next(walk(relative_to_path(TESTS_PATH)), (None, None, []))[2]
testvar = StringVar(canvas)
testvar.set(filenames[0])
test_options = OptionMenu(
    canvas,
    testvar,
    *filenames
)
test_options.place(
    x=835,
    y=53,
    width=130,
    height=25
)

####################################################

### Calibrations ###############################################################

# Calibration 1
canvas.create_text(
    66,
    156,
    anchor="nw",
    text="Calibration 1:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration1 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration1.place(
    x=66,
    y=176,
    width=160,
    height=43.5
)

# Calibration 2
canvas.create_text(
    295,
    156,
    anchor="nw",
    text="Calibration 2:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration2 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration2.place(
    x=295,
    y=176,
    width=160,
    height=43.5
)

# Calibration 3
canvas.create_text(
    523,
    156,
    anchor="nw",
    text="Calibration 3:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration3 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration3.place(
    x=523,
    y=176,
    width=160,
    height=43.5
)

# Calibration 4
canvas.create_text(
    751,
    156,
    anchor="nw",
    text="Calibration 4:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration4 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration4.place(
    x=751,
    y=176,
    width=160,
    height=43.5
)

# Calibration 5
canvas.create_text(
    66,
    312,
    anchor="nw",
    text="Calibration 5:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration5 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration5.place(
    x=66,
    y=332,
    width=160,
    height=43.5
)

# Calibration 6
canvas.create_text(
    295,
    312,
    anchor="nw",
    text="Calibration 6:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration6 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration6.place(
    x=295,
    y=332,
    width=160,
    height=43.5
)

# Calibration 7
canvas.create_text(
    523,
    312,
    anchor="nw",
    text="Calibration 7:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration7 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration7.place(
    x=523,
    y=332,
    width=160,
    height=43.5
)

# Calibration 8
canvas.create_text(
    751,
    312,
    anchor="nw",
    text="Calibration 8:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration8 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration8.place(
    x=751,
    y=331,
    width=160,
    height=43.5
)

# Calibration 9
canvas.create_text(
    66,
    466,
    anchor="nw",
    text="Calibration 9:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration9 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration9.place(
    x=66,
    y=486,
    width=160,
    height=43.5
)

# Calibration 10
canvas.create_text(
    295,
    466,
    anchor="nw",
    text="Calibration 10:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration10 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration10.place(
    x=295,
    y=486,
    width=160,
    height=43.5
)

# Calibration 11
canvas.create_text(
    523,
    466,
    anchor="nw",
    text="Calibration 11:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration11 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration11.place(
    x=523,
    y=486,
    width=160,
    height=43.5
)

# Calibration 12
canvas.create_text(
    751,
    466,
    anchor="nw",
    text="Calibration 12:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration12 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration12.place(
    x=751,
    y=486,
    width=160,
    height=43.5
)

# Calibration 13
canvas.create_text(
    66,
    620,
    anchor="nw",
    text="Calibration 13:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration13 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration13.place(
    x=66,
    y=640,
    width=160,
    height=43.5
)

# Calibration 14
canvas.create_text(
    295,
    620,
    anchor="nw",
    text="Calibration 14:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration14 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration14.place(
    x=295,
    y=640,
    width=160,
    height=43.5
)

# Calibration 15
canvas.create_text(
    523,
    620,
    anchor="nw",
    text="Calibration 15:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration15 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration15.place(
    x=523,
    y=640,
    width=160,
    height=43.5
)

# Calibration 16
canvas.create_text(
    751,
    620,
    anchor="nw",
    text="Calibration 16:",
    fill="#000000",
    font=("Roboto", 17 * -1)
)
calibration16 = Spinbox(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
calibration16.place(
    x=751,
    y=640,
    width=160,
    height=43.5
)

################################################################################

# App Window Settings
window.resizable(False, False)
window.mainloop()
