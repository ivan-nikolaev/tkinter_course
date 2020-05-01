# Create window class
from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")


window = Window()
window.mainloop()