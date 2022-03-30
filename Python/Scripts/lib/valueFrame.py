import tkinter as tk
from simpleUI import Frame
from tools import pad_text

class CheckFrame(Frame):
    checkbox = 0
    value = False
    label = ""
    pad_num = 20
    check_label = 0
    unmodified_label = ""
    
    def __init__(self, label, default_value=False, opt_width=1, opt_height=25, side=tk.LEFT, f_src=None):
        super().__init__(src=f_src)
        self.unmodified_label = label
        self.label = label.replace("-", "?").replace("_", " ")
        self.checkbox = self.add_check(pad_text(self.label, self.pad_num), opt_width, opt_height, side) # todo
        #self.add_label(pad_text(label, self.pad_num), opt_width, opt_height, side)
        self.value = default_value
        self.check_label = self.add_label(str(self.value), side)
    
    def update(self):
        self.value = self.get_check(self.checkbox) == 1
        self.update_label(self.check_label, pad_text(str(self.value), self.pad_num))
        
    def _close(self):
        self.quit()
        
    def get_value(self):
        return self.unmodified_label + str(self.value)
        

class ValueFrame(Frame):
    textbox = 0
    val_text = ""
    val_label = 0
    label = ""
    pad_num = 16
    unmodified_label = ""
    
    def __init__(self, label, units="", opt_width=1, opt_height=25, start_val=69, f_src=None):
        super().__init__(src=f_src)
        self.unmodified_label = label
        self.label = label.replace("-", "?").replace("_", " ")
        self.add_label(pad_text(self.label, self.pad_num), tk.LEFT)
        self.textbox = self.add_text_box(opt_width, opt_height, tk.LEFT)
        self.val_label = self.add_label("", tk.RIGHT)
        self.add_label(pad_text(" " + units), tk.RIGHT)
        self.update(text=str(start_val))
        
    def update(self, text=""):
        if len(text) == 0:
            text = self.get_text(self.textbox)
        if len(text) == 0:
            return
        self.val_text = text
        self.update_label(self.val_label, pad_text(text, self.pad_num))
    
    def get_value(self):
        return self.unmodified_label + str(self.val_text)
    
    def _close(self):
        self.quit()