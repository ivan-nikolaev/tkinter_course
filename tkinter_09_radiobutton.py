from tkinter import *
from tkinter import ttk


COLOR1 = 'Blue'
COLOR2 = 'Red'
COLOR3 = 'Gold'

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter OOP Window")
        self.minsize(500, 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.create_radio()

    def rad_event(self):
        rad_selected = self.radValues.get()

        if(rad_selected == 1):
            self.configure(background=COLOR1)
        elif (rad_selected == 2):
            self.configure(background=COLOR2)
        elif (rad_selected == 3):
            self.configure(background=COLOR3)


    def create_radio(self):
        self.radValues = IntVar()

        self.label = ttk.Label(self, text="Select Color")
        self.label.grid(column=0, row=0)

        self.rad1 = ttk.Radiobutton(self, text=COLOR1, value=1, variable=self.radValues,
                                    command=self.rad_event)
        self.rad1.grid(column=0, row=1, sticky=W, columnspan=3)

        self.rad2 = ttk.Radiobutton(self, text=COLOR2, value=2, variable=self.radValues,
                                    command=self.rad_event)
        self.rad2.grid(column=0, row=2, sticky=W, columnspan=3)

        self.rad3 = ttk.Radiobutton(self, text=COLOR3, value=3, variable=self.radValues,
                                    command=self.rad_event)
        self.rad3.grid(column=0, row=3, sticky=W, columnspan=3)

        self.button = ttk.Button(self, text="Click Me", command=self.click_me)
        self.button.grid(column=0, row=4)

    def click_me(self):
        #self.label.configure(text="Selected color: " + str(self.radValues.get()))
        pass

window = Window()
window.mainloop()