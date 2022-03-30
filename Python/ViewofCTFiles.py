#!/usr/bin/python3
import sys
from tkinter import Tk
import tkinter
sys.path.append('/home/sdaq/Scripts/lib')
#sys.path.append('C:\\Users\\hugh\\Documents\\SDAQ\\Python\\Scripts\\lib')
import tools
import simpleUI
class myFrame(simpleUI.Frame):
    myDirectory = 0
    myDirName = ""
    def __init__(self):
        self.textFrame = simpleUI.Frame()
        self.myDirectory = self.textFrame.add_label("Directory", tkinter.LEFT)
        self.textFrame.add_button("Update", 10, 1, "white", lambda: self.submission_command(), tkinter.RIGHT)
        self.textFrame.add_button("Notes", 10, 1, "white", lambda: print("hi"), tkinter.RIGHT)
        simpleUI.add_frame(self.textFrame)

    def submission_command(self):
        self.myDirName = tools.get_directory()
        self.textFrame.update_label(self.myDirectory, self.myDirName)
myFrame()
simpleUI.start_window()