from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.text_entry()

    def text_entry(self):
        self.name = StringVar()

        self.label = ttk.Label(self, text="Enter Your Name")
        self.label.grid(column=0, row=0)

        self.textbox = ttk.Entry(self, width=20, textvariable=self.name)
        self.textbox.grid(column=0, row=1)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=0, row=2)

    def click_me(self):
        self.label.configure(text="Hello "+self.name.get())

window = Window()
window.mainloop()