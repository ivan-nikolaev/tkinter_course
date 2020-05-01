
from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.create_checkbuttons()

    def create_checkbuttons(self):
        check1 = ttk.Checkbutton(self, text="Disabled", state='disabled')
        check1.grid(column=0, row=0)

        check2 = ttk.Checkbutton(self, text="Unchecked")
        check2.grid(column=1, row=0)

        check3 = ttk.Checkbutton(self, text="Enabled")
        check3.grid(column=2, row=0)

window = Window()
window.mainloop()