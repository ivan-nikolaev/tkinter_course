
from tkinter import *

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter Label")
        self.minsize('500', 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.createLabel()

    def createLabel(self):
        labelFont = ('times', 40, 'bold')
        label = Label(self, text = 'Label Creation')
        label.config(font = labelFont, bg = 'black', fg = 'yellow')
        label.grid(column=0, row=0)

window = Window()
window.mainloop()