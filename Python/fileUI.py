import tkinter as tk
import sys

sys.path.append('/home/sdaq/Scripts/lib')
import simpleUI
from valueFrame import ValueFrame, CheckFrame
from tools import *

class ClutchesFileUI(simpleUI.Frame):
    option_frames = []
    notes_text = ""
    
    def __init__(self, updateEvent, clutches_options=[], clutches_checks=[], f_src=None):
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
        
        def update_all():
            notes_text = notes_frame.get_text(notes).replace("Run", "run")
            
            for frame in self.option_frames:
                frame.update()
        
        options_frame.add_label("  ", tk.BOTTOM)
        simpleUI.add_frame(options_frame, window_side=tk.TOP)
        notes_frame.add_label("Notes:", tk.TOP)
        notes = notes_frame.add_text_box(3, 100, tk.BOTTOM)
        simpleUI.add_frame(notes_frame)
        update_frame = simpleUI.Frame(src=self)
        update_frame.add_label(" ", tk.TOP)
            
        path_field = ""
        path_text = update_frame.add_label("", tk.BOTTOM)
        def update(beginning=False):
            updateEvent(self.option_frames, notes, update_frame, path_text, beginning) # TODO
        update(beginning=True)
        
        update_frame.add_button("Update", 10, 1, "white", update_all, tk.TOP)
        
        simpleUI.add_frame(update_frame, window_side=tk.TOP)
        
    def get_notes(self):
        return notes_text
        
            
