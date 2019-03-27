from tkinter import *
import tkinter as tk

import final_drill_gui
import final_drill_func
                        

class MainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
    
        self.master = master
        self.master.minsize(800,330) 
        self.master.maxsize(800,330)
        self.master.title("Files Transfer")
        self.master.configure(bg="#F0F0F0")
        final_drill_func.center_window(self,800,300)
        
#GUI widgets connected to the program functions

        final_drill_gui.window_gui(self)


if __name__ == "__main__":
    root = Tk()
    App = MainWindow(root)
    root.mainloop()
