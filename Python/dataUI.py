import tkinter as tk
import sys

sys.path.append('/home/sdaq/Scripts/lib')
import simpleUI
from tools import *

class ClutchesDataUI(simpleUI.Frame):
    running_label = 0
    time_box = 0
    
    def __init__(self, startFn, stopFn, timeUpdateEvent):
        super().__init__()
        self.add_label(" ", tk.TOP)
        time_frame = simpleUI.Frame(src=self)
        time_frame.add_label("Time: ", tk.LEFT)
        self.time_box = time_frame.add_text_box(1, 25, tk.LEFT)
        def set_time():
            timeUpdateEvent(self.get_text(self.time_box)) # todo
        time_frame.add_button("Set", 5, 1, "lightgray", set_time, tk.RIGHT)
        simpleUI.add_frame(time_frame, tk.TOP)
        self.running_label = self.add_label("Running: False", tk.TOP)
        self.add_label(" ", tk.TOP)
        button_frame = simpleUI.Frame(src=self)
        button_frame.create_cat_jam(label_side=tk.LEFT, label_anchor=tk.SW, flipped=True)
        button_frame.add_button("Start", 25, 5, "green", startFn, tk.LEFT)
        button_frame.create_cat_jam(label_side=tk.RIGHT, label_anchor=tk.SE)
        button_frame.add_button("Stop", 25, 5, "red", stopFn, tk.RIGHT)
        simpleUI.add_frame(button_frame)
        
    def update_running_label(self, collecting):
        self.update_label(self.running_label, "Running: " + str(collecting))