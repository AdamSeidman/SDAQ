import tkinter as tk
from simpleUI import Frame

class valueFrame(Frame):
    
    def __init__(self):
        super().__init__()
    
    def _close(self):
        self.quit()
        
    
    def add_options(self, optText1, optWidth1, optHeight1, txt1, value1, optText2, optWidth2, optHeight2, txt2, value2):
        updating_text_boxes = []
        updating_labels = []
        if txt1:
            self.add_label(optText1, optWidth1, optHeight1, tk.LEFT)
            temp = self.add_text_box(optWidth1, optHeight1, tk.LEFT)
            updating_text_boxes.append(temp)
            temp = self.add_label("Current Value: " + str(value1) + "\t", 1, 25, tk.LEFT)
            updating_labels.append(temp)
            
        else:
            temp = self.add_check(optText1, optWidth1, optHeight1, value1, tk.LEFT)
            updating_text_boxes.append(temp)
            temp = self.add_label("   Current? " + ('True' if value1.get() == 1 else 'False') + "\t    ", 1, 25, tk.LEFT)
            updating_labels.append(temp)
        
        if txt2:
            temp = self.add_label("Current Value: " + str(value2) + "\t", 1, 25, tk.RIGHT)
            updating_labels.append(temp)
            temp = self.add_text_box(optWidth2, optHeight2, tk.RIGHT)
            updating_text_boxes.append(temp)
            self.add_label(optText2, optWidth2, optHeight2, tk.RIGHT)
        else:
            temp = self.add_label("   Current? " + ('True' if value2.get() == 1 else 'False') + "\t    ", 1, 25, tk.RIGHT)
            updating_labels.append(temp)
            temp = self.add_check(optText2, optWidth2, optHeight2, value2, tk.RIGHT)
            updating_text_boxes.append(temp)
        return updating_text_boxes, updating_labels