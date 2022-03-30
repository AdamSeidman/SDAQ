import tkinter as tk
from tkinter import PhotoImage
import time
import os

window = tk.Tk()

class Frame(tk.Frame):
    __labels = []
    __text_boxes = []
    __cat_jam_labels = []
    __frames = []
    
    def __init__(self, border_color=None, border_width=0, src=None):
        global window
        super().__init__(highlightbackground=border_color, highlightthickness=border_width, master=src)
    
    def _close(self):
        self.quit()
    
    def add_button(self, btnText, btnWidth, btnHeight, bkg, cmd, btnSide, btnAnchor=None):
        if len(bkg) == 0:
            bkg = "white"
        frg = "black"
        if bkg == "black":
            frg = "white"
        btn = tk.Button(
            self,
            text=btnText,
            width=btnWidth,
            height=btnHeight,
            bg=bkg,
            fg=frg,
            command=cmd
        )
        btn.pack(side=btnSide,anchor=btnAnchor)
    
    def add_check(self, checkText, checkHeight, checkWidth, checkSide):
        var = tk.IntVar()
        check = tk.Checkbutton(
            self,
            text=checkText,
            width=checkWidth,
            height=checkHeight,
            variable=var
        )
        self.__text_boxes.append(var)
        check.pack(side=checkSide)
        return len(self.__text_boxes) - 1
    
    def get_check(self, chNum):
        if chNum >= len(self.__text_boxes):
            return False
        return self.__text_boxes[chNum].get()
    
    def add_label(self, labelText, labelSide, labelAnchor=None):
        i = len(self.__labels)
        self.__labels.append(tk.StringVar())
        self.__labels[i].set(labelText)
        label = tk.Label(self, textvariable=self.__labels[i])
        label.pack(side=labelSide, anchor=labelAnchor)
        return i
    
    def update_label(self, labelNum, labelText):
        if labelNum >= len(self.__labels):
            return
        self.__labels[labelNum].set(labelText)
    
    def add_text_box(self, tbHeight, tbWidth, tbSide):
        textBox = tk.Text(self, height=tbHeight, width=tbWidth)
        textBox.pack(side=tbSide)
        self.__text_boxes.append(textBox)
        return len(self.__text_boxes) - 1
    
    def get_text(self, tbNum):
        if tbNum >= len(self.__text_boxes):
            return ""
        return self.__text_boxes[tbNum].get("1.0", "end-1c")
    
    def create_cat_jam(self, label_side=tk.TOP, label_anchor=tk.NE, flipped=False):
        url='/home/sdaq/Scripts/assets/cat_jam.gif'
        numFrames = 87
        if flipped:
            url='/home/sdaq/Scripts/assets/cat_jam2.gif'
        label_index = len(self.__frames)
        self.__frames.append([PhotoImage(file=url, format = 'gif -index %i' %(i)) for i in range(numFrames)])
        self.__cat_jam_labels.append(tk.Label(self))
        def update_img(ind):
            frame = self.__frames[label_index][ind]
            ind += 1
            if ind == numFrames:
                ind = 0
            self.__cat_jam_labels[label_index].configure(image=frame)
            window.after(100, update_img, ind)
        update_img(0)
        self.__cat_jam_labels[label_index].pack(side=label_side, anchor=label_anchor)

def set_title(title):
    global window
    window.title(title)
    
def add_frame(frame, window_side=tk.TOP, window_anchor=None):
    frame.pack(side=window_side, anchor=window_anchor)

def add_main_event(event):
    global window
    window.after(1, lambda: __sub_event_func(event))

def __sub_event_func(event):
    global window
    event()
    window.after(1, lambda: __sub_event_func(event))

def start_window():
    global window
    #window.after(0, update_img, 0)
    window.mainloop()
