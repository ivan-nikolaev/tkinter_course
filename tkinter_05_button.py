from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter Label")
        self.minsize('500', 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.label = ttk.Label(self, text='Tkinter Application')
        self.label.grid(column=1, row=0)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=0, row=0)



    def click_me(self):
        self.label.configure(text='Text Is Changed')
        self.label.configure(foreground='red', background='yellow')
        self.button.configure(text='Button Changed')

window = Window()
window.mainloop()