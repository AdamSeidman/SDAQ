import matplotlib.pyplot as plt
import numpy as np

DEFAULT_LINE_TYPE = ".b-"
lines = []
figures = []
axs = []

plt.ion()

def create_plot(firstLineType):
	global figures, lines, axs
	figure, ax = plt.subplots()
	ax.set_autoscalex_on(True)
	ax.set_autoscaley_on(True)
	ax.grid()
	figures.append(figure)
	axs.append(ax)
	lines.append([])
	plotNum = len(lines) - 1
	create_line(plotNum, firstLineType)
	plot(plotNum, 0, [], [])
	return plotNum

def set_title(plotNum, title):
	global plt
	plt.title(title)
	
def set_labels(plotNum, xlabel, ylabel):
	global plt
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

def create_line(plotNum, lineType):
	global axs, lines
	if plotNum >= len(lines):
		return -1
	if len(lineType) == 0:
		lineType = DEFAULT_LINE_TYPE
	line, = axs[plotNum].plot([], [], lineType)
	lines[plotNum].append(line)
	return len(lines[plotNum]) - 1

def plot(plotNum, lineNum, xData, yData):
	global lines, axs, figures
	if plotNum >= len(lines):
		return False
	while len(lines[plotNum]) <= lineNum:
		create_line(DEFAULT_LINE_TYPE)
	lines[plotNum][lineNum].set_xdata(xData)
	lines[plotNum][lineNum].set_ydata(yData)
	axs[plotNum].relim()
	axs[plotNum].autoscale_view()
	figures[plotNum].canvas.draw()
	figures[plotNum].canvas.flush_events()
	return True
