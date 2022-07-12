import sys

#sys.path.append("fjdshoinfds\sdaq-git\lib")
sys.path.append("C:/Users/Adam/Documents/#Code/SDAQ/Python/lib")

import tools
import sdaq
import graphing

sensorNumber = 3

sdaq.create_i2c_bus()
boardNumber = sdaq.get_active_i2c_devices()[0]

'''
xData = [0]
    yData = [0]
    lastTickTime = -1000.0
    lastTick = 0
    for tick in ticks:
        if not (tick[0] == lastTick) and ((tick[0] == 255) or (tick[0] == 1)):
            xData.append(tick[1])
            yData.append((((1.0 / (tick[1] - lastTickTime)) * 60.0) / tpr))
            lastTickTime = tick[1]
        lastTick = tick[0]
'''

tools.reset_time()
lastTick = tools.get_time()
tick = 1.0

plot = graphing.Plot()

while True:
    pass