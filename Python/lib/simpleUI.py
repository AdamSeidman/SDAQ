import tkinter as tk

window = tk.Tk()

class Frame(tk.Frame):
    __labels = []
    __text_boxes = []
    
    def __init__(self):
        global window
        super().__init__(window)
    
    def _close(self):
        self.quit()
    
    def add_button(self, btnText, btnWidth, btnHeight, bkg, cmd, btnSide):
        if len(bkg) == 0:
            bkg = "white"
        frg = "black"
        if bkg == "black":
            frg = "white"
        btn = tk.Button(
            self,
            text=btnText,
            width=btnWidth,
            height=btnHeight,
            bg=bkg,
            fg=frg,
            command=cmd
        )
        btn.pack(side=btnSide)
    
    def add_label(self, labelText, labelWidth, labelHeight, labelSide):
        i = len(self.__labels)
        self.__labels.append(tk.StringVar())
        self.__labels[i].set(labelText)
        label = tk.Label(self, textvariable=self.__labels[i])
        label.pack(side=labelSide)
        return i
    
    def update_label(self, labelNum, labelText):
        if labelNum >= len(self.__labels):
            return
        self.__labels[labelNum].set(labelText)
    
    def add_text_box(self, tbHeight, tbWidth, tbSide):
        textBox = tk.Text(self, height=tbHeight, width=tbWidth)
        textBox.pack(side=tbSide)
        self.__text_boxes.append(textBox)
        return len(self.__text_boxes) - 1
    
    def get_text(self, tbNum):
        if tbNum >= len(self.__text_boxes):
            return ""
        return self.__text_boxes[tbNum].get("1.0", "end-1c")
        
def set_title(title):
    global window
    window.title(title)
    
def add_frame(frame, window_side=tk.TOP):
    frame.pack(side=window_side)

def add_main_event(event):
    global window
    window.after(1, lambda: __sub_event_func(event))

def __sub_event_func(event):
    global window
    event()
    window.after(1, lambda: __sub_event_func(event))

def start_window():
    global window
    window.mainloop()
