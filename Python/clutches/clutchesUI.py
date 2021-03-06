import tkinter as tk
import sys
from dataUI import ClutchesDataUI
from fileUI import ClutchesFileUI

sys.path.append('/home/sdaq/Scripts/lib')
import simpleUI

def doNothing(): # todo ?
    pass

class ClutchesUI():
    fileUI = None
    dataUI = None
    
    def __init__(self, title, clutches_options, clutches_checks, startFn=doNothing, stopFn=doNothing, fileUpdateFn=doNothing, timeSetFn=doNothing):
        self.fileUI = ClutchesFileUI(fileUpdateFn, clutches_options, clutches_checks)
        self.dataUI = ClutchesDataUI(startFn, stopFn, timeSetFn)
        simpleUI.set_title(title)
        simpleUI.add_frame(self.fileUI, tk.TOP)
        simpleUI.add_frame(self.dataUI, tk.BOTTOM)
        
    def start_main_event(self, event):
        simpleUI.add_main_event(event)
        simpleUI.start_window()
        
    def update_running_label(self, collecting):
        self.dataUI.update_running_label(collecting)
        
    