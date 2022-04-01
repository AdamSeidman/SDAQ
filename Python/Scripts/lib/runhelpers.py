import re
import ast
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
    def __init__(self, dir_name: str, name: str):
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