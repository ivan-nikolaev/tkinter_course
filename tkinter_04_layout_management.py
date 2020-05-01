from tkinter import *

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title("Tkinter Label")
        self.minsize('500', 400)
        self.wm_iconbitmap("resourses/virus_coronavirus_medical_bacterium_cell_icon_142127.ico")

        self.create_layout()

    def create_layout(self):
        Label(self, text = "Pack Layuot Example").pack()
        Button(self, text = "Not Going To Be Expand").pack()
        Button(self, text="It Expand An Not Fill x").pack(expand=1)
        Button(self, text="Fill x and Expand").pack(fill=X, expand=1)

        Button(self, text='Left').pack(side=LEFT)
        Button(self, text='Center').pack(side=RIGHT)
        Button(self, text='Right').pack(side=RIGHT)

        Button(self, text='Absolute Position').place(x=100,y=150)
        Button(self, text='Relative Position').place(relx=0.8, rely=0.9, relwidth=10, anchor=NE)

window = Window()
window.mainloop()