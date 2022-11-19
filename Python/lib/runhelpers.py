import re
import ast
import sys
class RunDump():
    def __init__(self, runNum, xvals, yvals, runTime):
        self.runNum = runNum
        self.xvals = xvals
        self.yvals = yvals
        self.runTime = runTime
    def get_xvals(self) -> list[float]:
        return self.xvals
    def get_yvals(self) -> list[float]:
        return self.yvals
    def get_runName(self) -> int:
        return self.runNum
    def get_runTime(self) -> float:
        return self.runTime
class FileInfo():
    fileName = ""
    fileSetup = 0
    numRuns = 0
    setupName = ""
    avgTime = 0.0
    totalTime = 0.0
    fastestTime = 0.0
    def __init__(self, dir_name: str, name: str):
        self.fileName = name
        m = re.match("[0-9]*", name)
        if m is None:
            exit(1)
        self.fileSetup = int(m.group())
        self.setupName = name[name.find(str(m)):-3]
        file = open(dir_name + '/' + self.fileName, "r")
        lines = file.readlines()
        lineNum = 0
        has_a_run_been_found = False
        notesStart = 1
        notesEnd = 0
        self.runs = []
        self.notes = ""
        while lineNum < len(lines):
            if lines[lineNum].startswith("Run"):
                matchGroup = re.findall("(\d+.\d+|\d+)", lines[lineNum])
                if not has_a_run_been_found:
                    notesEnd = lineNum
                    self.notes = '\n'.join(lines[notesStart:notesEnd])
                    has_a_run_been_found = True
                xvals = ast.literal_eval(lines[lineNum + 1])
                self.runs.append(RunDump(int(matchGroup[0]), xvals, ast.literal_eval(lines[lineNum + 2]), float(matchGroup[1])))
                lineNum = lineNum + 1
            lineNum = lineNum + 1
    def get_average_time(self) -> float:
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
    def get_total_time(self) -> float:
        if self.totalTime != 0:
            return self.totalTime
        running_total = 0.0
        for run in self.runs:
            running_total = running_total + run.get_runTime()
        self.totalTime = running_total
        return self.totalTime
    def get_fastest_time(self) -> float:
        if self.fastestTime != 0:
            return self.fastestTime
        self.fastestTime = min(self.runs, key=lambda x: x.get_runTime()).get_runTime()
        return self.fastestTime
    def get_setup_number(self) -> int:
        return self.fileSetup
    def get_name(self)  -> str:
        return self.fileName
    def get_notes(self) -> str:
        return self.notes
    def get_runs(self) -> list[RunDump]:
        return self.runs