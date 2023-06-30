#!/usr/bin/python3
import sys
from tkinter import HORIZONTAL, RIGHT, TOP, VERTICAL, Y, Scrollbar, StringVar, Tk
import tkinter
import os
from typing import Literal

#sys.path.append('/media/sdaq/USB DISK2lib')
#sys.path.append('C:\\Users\\hugh\\Documents\\SDAQ\\Python\\Scripts\\lib')
path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, "..", "lib")
path = os.path.abspath(path)
sys.path.append(path)

#sys.path.append('Scripts\\lib')
import tools
import simpleUI
import graphing
import runhelpers

dir_name = ""

class myFrame(simpleUI.Frame):
    myDirectory = 0
    myDirName = ""
    ctfiles = None
    lineList = list()
    plt = None
    myCanvas = None
    myScrollbar = None
    sorting_type = StringVar()
    radio_list = []
    def __init__(self):
        self.masterFrame = simpleUI.Frame()
        self.textFrame = simpleUI.Frame(src=self.masterFrame)
        self.myDirectory = self.textFrame.add_label("No directory has been chosen", tkinter.LEFT)
        self.textFrame.add_button("Update", 10, 1, "white", lambda: self.update_command(), tkinter.RIGHT)
        self.textFrame.add_button("Select Directory", 20, 1, "white", lambda: self.submission_command(), tkinter.RIGHT)
        self.sorting_type=StringVar(value="setup_num")
        self.radio_list.append(tkinter.Radiobutton(master=self.textFrame, text="Setup Number", variable=self.sorting_type, value="setup_num"))
        self.radio_list[0].pack(side=tkinter.RIGHT)
        self.radio_list.append(tkinter.Radiobutton(master=self.textFrame, text="Fastest time", variable=self.sorting_type, value="fastest_time"))
        self.radio_list[1].pack(side=tkinter.RIGHT)
        self.RunsFrame = simpleUI.Frame(border_color='black', border_width=1, src=self.masterFrame)
        self.myCanvas = tkinter.Canvas(master=self.RunsFrame)
        self.myCanvas.pack(side=tkinter.LEFT)
        self.myScrollbar = Scrollbar(self.RunsFrame, orient=VERTICAL)
        self.myScrollbar.pack(side=RIGHT, fill=Y)
        self.myCanvas.config(xscrollcommand=self.myScrollbar.set)
        simpleUI.add_frame(self.masterFrame)
        simpleUI.add_frame(self.textFrame)
        simpleUI.add_frame(self.RunsFrame)
        simpleUI.set_minsize_of_window(250, 200)
        simpleUI.set_title("Clutchtuning viewer")
    def update_command(self):
        self.files = []
        self.ctfiles = list(filter(lambda x: x.endswith(".ct"), os.listdir(self.myDirName)))
        for ctfile in self.ctfiles:
            self.files.append(runhelpers.FileInfo(self.myDirName,ctfile))
        max_button_size = 10
        for child in self.myCanvas.winfo_children():
            child.destroy()
        self.files.sort(key=lambda x: x.get_setup_number())
        if self.sorting_type.get() == "fastest_time":
            self.files.sort(key=lambda x: x.get_fastest_time())
        for file in self.files:
            max_button_size = max(max_button_size, len(file.fileName))
            newChild = simpleUI.Frame(border_color="black", border_width=1, src=self.myCanvas)
            newChild.add_label("Setup Number: {}".format(file.get_setup_number()), tkinter.LEFT)
            newChild.add_label(file.get_name(), tkinter.LEFT)
            newChild.add_label("Average: {}".format(file.get_average_time()), tkinter.LEFT)
            newChild.add_label("Fastest: {}".format(file.get_fastest_time()), tkinter.LEFT)
            newChild.add_button("Notes", len("Notes"), 1, "grey", lambda: self.make_notes_window(file), tkinter.LEFT)
            newChild.add_button("View graphs", len("View graphs"), 1, "gray", lambda: self.make_graph_window(file), tkinter.LEFT)
            simpleUI.add_frame(newChild)
    def submission_command(self):
        global dir_name
        self.myDirName = tools.get_directory()
        dir_name = self.myDirName
        self.textFrame.update_label(self.myDirectory, self.myDirName)
    def make_notes_window(self, file: runhelpers.FileInfo):
        topLevel = tkinter.Toplevel(self.masterFrame)
        topLevel.title("Notes")
        tempFrame = simpleUI.Frame(src=topLevel)
        simpleUI.add_frame(tempFrame)
        tempFrame.add_label(file.get_notes(), TOP)
        topLevel.minsize(250, 250)
    def make_graph_window(self, file: runhelpers.FileInfo):
        plt = graphing.Plot()
        plt.update_title("All runs")
        for i in range(len(file.get_runs())):
            self.lineList.append(i)
            plt.plot(i, file.get_runs()[i].xvals, file.get_runs()[i].yvals)

myFrame()
simpleUI.start_window()