#!/usr/bin/python3
from asyncio.base_tasks import _task_print_stack
import sys
from tkinter import VERTICAL, Tk
import re
import tkinter
import ast
import os
#sys.path.append('/home/sdaq/Scripts/lib')
sys.path.append('C:\\Users\\hugh\\Documents\\SDAQ\\Python\\Scripts\\lib')
#sys.path.append('Scripts\\lib')
import tools
import simpleUI
import graphing

dir_name = ""

class RunDump():
    def __init__(self, runNum, xvals, yvals, runTime, notes=""):
        self.runNum = runNum
        self.xvals = xvals
        self.yvals = yvals
        self.runTime = runTime
        self.notes = ""
    def get_xvals(self):
        return self.xvals
    def get_yvals(self):
        return self.yvals
    def get_runName(self):
        return self.runNum
    def get_runTime(self) -> float:
        return self.runTime
    def get_notes(self):
        return self.notes
class FileInfo():
    fileName = ""
    fileSetup = 0
    numRuns = 0
    setupName = ""
    avgTime = 0.0
    totalTime = 0.0
    fastestTime = 0.0
    def __init__(self, name: str):
        self.fileName = name
        m = re.match("[0-9]*", name)
        if m is None:
            exit(1)
        self.fileSetup = m.group()
        self.setupName = name[name.find(str(m)):-3]
        file = open(dir_name + self.fileName, "r")
        lines = file.readlines()
        lineNum = 0
        has_a_run_been_found = False
        notesStart = 1
        notesEnd = 0
        self.runs = []
        self.notes = ""
        while lineNum < len(lines):
            regmatch = re.search("Run ([0-9]*): ([0-9]*\.{0,1}[0-9]*) s", lines[lineNum])
            if regmatch is not None:
                if not has_a_run_been_found:
                    notesEnd = lineNum
                    self.notes = '\n'.join(lines[notesStart:notesEnd])
                    has_a_run_been_found = True
                xvals = ast.literal_eval(lines[lineNum + 1])
                print(regmatch.group(1))
                self.runs.append(RunDump(int(regmatch.group(1)), xvals, ast.literal_eval(lines[lineNum + 2]), float(regmatch.group(2))))
                lineNum = lineNum + 1
            lineNum = lineNum + 1
    def get_average_time(self):
        if self.avgTime != 0:
            return self.avgTime
        running_total = 0.0
        for run in self.runs:
            running_total = running_total + run.get_runTime()
        try:
            self.avgTime = running_total / len(self.runs)
        except ZeroDivisionError:
            self.avgTime = 0
        self.totalTime = running_total
        return self.avgTime
    def get_total_time(self):
        if self.totalTime != 0:
            return self.totalTime
        running_total = 0.0
        for run in self.runs:
            running_total = running_total + run.get_runTime()
        self.totalTime = running_total
        return self.totalTime
    def get_fastest_time(self):
        if self.fastestTime != 0:
            return self.fastestTime
        for time in self.runs:
            self.fastestTime = max(time.get_runTime(), self.fastestTime)
        return self.fastestTime
    def get_setup_number(self):
        return self.fileSetup
    def get_name(self):
        return self.fileName
    def get_notes(self):
        return self.notes
    def get_runs(self) -> list[RunDump]:
        return self.runs
        
class myFrame(simpleUI.Frame):
    myDirectory = 0
    myDirName = ""
    ctfiles = None
    files = list()
    lineList = list()
    def __init__(self):
        self.masterFrame = simpleUI.Frame()
        self.textFrame = simpleUI.Frame(src=self.masterFrame)
        self.myDirectory = self.textFrame.add_label("No directory has been chosen", tkinter.LEFT)
        self.textFrame.add_button("Update", 10, 1, "white", lambda: self.update_command(), tkinter.RIGHT)
        self.textFrame.add_button("Select Directory", 20, 1, "white", lambda: self.submission_command(), tkinter.RIGHT)
        self.RunsFrame = simpleUI.Frame(border_color='black', border_width=1, src=self.masterFrame)
        simpleUI.add_frame(self.masterFrame)
        simpleUI.add_frame(self.textFrame)
        simpleUI.add_frame(self.RunsFrame)
        simpleUI.set_minsize_of_window(250, 200)
        simpleUI.set_title("Clutchtuning viewer")
    def update_command(self):
        self.ctfiles = list(filter(lambda x: x.endswith(".ct"), os.listdir(self.myDirName)))
        for ctfile in self.ctfiles:
            self.files.append(FileInfo(ctfile))
        max_button_size = 10
        for child in self.RunsFrame.winfo_children():
            child.destroy()
        for file in self.files:
            max_button_size = max(max_button_size, len(file.fileName))
            newChild = simpleUI.Frame(border_color="black", border_width=1, src=self.RunsFrame)
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
    def make_notes_window(self, file: FileInfo):
        topLevel = tkinter.Toplevel(self.masterFrame)
        topLevel.title("Notes")
        print(file.get_notes())
        tkinter.Label(topLevel, textvariable=tkinter.StringVar().set(file.get_notes()))
        
    def make_graph_window(self, file: FileInfo):
        plt = graphing.Plot()
        plt.set_title("All runs")
        for i in range(len(file.get_runs())):
            self.lineList.append(i)
            plt.plot(i, file.get_runs()[i].xvals, file.get_runs()[i].yvals)

myFrame()
simpleUI.start_window()