from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.create_combo()

    def create_combo(self):
        self.language = StringVar()

        self.combobox = ttk.Combobox(self, width=20, textvariable = self.language)
        self.combobox['values'] = ("Python", "Java", "PHP", "C++")
        self.combobox.grid(column=1, row=1)

        self.label = ttk.Label(self, text="Select Your Language")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=0, row=2)

    def click_me(self):
        self.label.configure(text="Selected: "+self.language.get())

window = Window()
window.mainloop()