import tkinter as tk
import sys

path = os.path.dirname(os.path.abspath(__file__))
path = path + "\\..\\lib"
path = os.path.abspath(path)
sys.path.append(path)

import simpleUI
from valueFrame import ValueFrame, CheckFrame
from tools import *

class ClutchesFileUI(simpleUI.Frame):
    option_frames = []
    notes_text = ""
    
    def __init__(self, updateEvent, clutches_options=[], clutches_checks=[]):
        super().__init__(border_color='black', border_width=1)
        
        currentFrame = None

        notes_frame = simpleUI.Frame(src=self)
        options_button_frame = simpleUI.Frame(src=self)
        
        use_left = True
        options_frame = simpleUI.Frame(src=self)
        left_frame = simpleUI.Frame(src=options_frame)
        right_frame = simpleUI.Frame(src=options_frame)
        
        for option in clutches_options:
            parent_frame = right_frame
            if use_left:
                parent_frame = left_frame
            valFrame = ValueFrame(label=option[0], units=option[1], f_src=parent_frame)
            self.option_frames.append(valFrame)
            simpleUI.add_frame(valFrame, window_side=tk.TOP)
            use_left = not use_left

        for check in clutches_checks:
            parent_frame = right_frame
            if use_left:
                parent_frame = left_frame
            checkFrame = CheckFrame(check[0], default_value=check[1], f_src=parent_frame)
            self.option_frames.append(checkFrame)
            simpleUI.add_frame(checkFrame, window_side=tk.TOP)
            use_left = not use_left
        
        simpleUI.add_frame(left_frame, window_side=tk.LEFT)
        simpleUI.add_frame(right_frame, window_side=tk.RIGHT)
        simpleUI.add_frame(options_button_frame, window_side=tk.TOP)
        
        options_frame.add_label("  ", tk.BOTTOM)
        simpleUI.add_frame(options_frame, window_side=tk.TOP)
        notes_frame.add_label("Notes:", tk.TOP)
        notes = notes_frame.add_text_box(3, 100, tk.BOTTOM)
        simpleUI.add_frame(notes_frame)
        update_frame = simpleUI.Frame(src=self)
        update_frame.add_label(" ", tk.TOP)
            
        path_field = ""
        path_text = update_frame.add_label("No File Created Yet", tk.BOTTOM)
        
        def update(): # do we need to run this immediately after?
            notes_text = notes_frame.get_text(notes).replace("Run", "run")
            builder = ""
            for frame in self.option_frames:
                frame.update()
                builder += frame.get_value()
            filename = updateEvent(builder, notes_text)
            update_frame.update_label(path_text, "Current File: " + str(filename))
        
        update_frame.add_button("Update", 10, 1, "white", update, tk.TOP)
        
        simpleUI.add_frame(update_frame, window_side=tk.TOP)
        
    def get_notes(self):
        return notes_text
        
            
