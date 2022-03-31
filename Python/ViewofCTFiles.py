#!/usr/bin/python3
import sys
from tkinter import Tk
import re
import tkinter
import ast
import os
#sys.path.append('/home/sdaq/Scripts/lib')
sys.path.append('C:\\Users\\hugh\\Documents\\SDAQ\\Python\\Scripts\\lib')
import tools
import simpleUI
class RunDump():
    def __init__(self, runNum, xvals, yvals, runTime):
        self.runNum = runNum
        self.xvals = xvals
        self.yvals = yvals
        self.runTime = runTime
    def get_xvals(self):
        return self.xvals
    def get_yvals(self):
        return self.yvals
    def get_runName(self):
        return self.runNum
    def get_runTime(self):
        return self.runTime
class FileInfo():
    fileName = ""
    fileSetup = 0
    totalTime = 0.0
    numRuns = 0
    setupName = ""
    runs = list()
    def __init__(self, name: str):
        self.fileName = name
        m = re.match("[0-9]*")
        if m is None:
            exit(1)
        self.fileSetup = m.group()
        self.setupName = name[name.find():-3]
        file = open("r", self.fileName)
        lines = file.readlines()
        lineNum = 0
        
        while lineNum < len(lines):
            regmatch = re.search("Run ([0-9]*): ([0-9]*\.{0,1}[0-9]*", lines[lineNum])
            if regmatch is not None:
                self.runs.append(RunDump(regmatch.group(0), ast.literal_eval(lines[lineNum + 1]), ast.literal_eval(lines[lineNum + 2]), regmatch.group(1)))
                lineNum = lineNum + 1
            lineNum = lineNum + 1
    def get_average_time(self):
        running_total = 0.0
        for run in self.runs:
            running_total = running_total + run.get_runTime()
        return running_total / len(self.runs)
    def get_total_time(self):
        running_total = 0.0
        for run in self.runs:
            running_total = running_total + run.get_runTime()
        return running_total
        
class myFrame(simpleUI.Frame):
    myDirectory = 0
    myDirName = ""
    ctfiles = None
    files = list()
    def __init__(self):
        self.textFrame = simpleUI.Frame()
        self.myDirectory = self.textFrame.add_label("Directory", tkinter.LEFT)
        self.textFrame.add_button("Select Directory", 10, 1, "white", lambda: self.submission_command(), tkinter.RIGHT)
        self.textFrame.add_button("Update", 10, 1, "white", lambda: self.update_command(), tkinter.RIGHT)
        self.RunsFrame = simpleUI.Frame()
        simpleUI.add_frame(self)
    def update_command(self):
        self.ctfiles = list(filter(lambda x: x.endswith(".ct"), os.listdir(self.myDirName)))
        for ctfile in self.ctfiles:
            self.files.append(FileInfo(ctfile))
    def submission_command(self):
        self.myDirName = tools.get_directory()
        self.textFrame.update_label(self.myDirectory, self.myDirName)
myFrame()
simpleUI.start_window()