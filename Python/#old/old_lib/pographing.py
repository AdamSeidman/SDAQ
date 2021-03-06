import matplotlib.pyplot as plt

DEFAULT_LINE_TYPE = ".b-"

plt.ion()

class Plot:
    __lines = []
    __ax = None
    __figure = None
    
    def __init__(self, line_type=DEFAULT_LINE_TYPE, title="", xlabel="", ylabel=""):
        self.__figure, self.__ax = plt.subplots()
        self.__ax.set_autoscalex_on(True)
        self.__ax.set_autoscaley_on(True)
        self.__ax.grid()
        self.create_line(line_type)
        self.plot(0, [], [])
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def create_line(self, line_type=DEFAULT_LINE_TYPE):
        if len(line_type) == 0:
            line_type = DEFAULT_LINE_TYPE
        line, = self.__ax.plot([], [], line_type)
        self.__lines.append(line)
        return len(self.__lines) - 1

    def set_title(self, title): #todo
        plt.title(title)

    def plot(self, line_num, xData, yData):
        while len(self.__lines) <= line_num:
            self.create_line()
        self.__lines[line_num].set_xdata(xData)
        self.__lines[line_num].set_ydata(yData)
        self.__ax.relim()
        self.__ax.autoscale_view()
        self.__figure.canvas.draw()
        self.__figure.canvas.flush_events()
