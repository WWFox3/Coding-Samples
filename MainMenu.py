## This program was made by William W Fox III
## The program here is a attempt at making a text based adventure.

import tkinter
import tkinter.messagebox

class OpeningScreen:
    def __init__(self):
        self.main_menu = tkinter.Tk()
        self.label = tkinter.Label(self.main_menu, text = "Never Ending Quest")

        self.label.pack()
        
        tkinter.mainloop()

Opening_Screen = OpeningScreen()

        
