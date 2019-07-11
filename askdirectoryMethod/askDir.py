from tkinter import *
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        def dirSearch():
            dir_path=filedialog.askdirectory(parent=root,initialdir="/",title='Pick a directory')
            if dir_path:
                self.txt_dPath.insert(INSERT,dir_path)
            

        self.master = master
        self.master.minsize(600,250) 
        self.master.maxsize(600,250)
        self.master.title("Directory Search")
        self.master.configure(bg="#F0F0F0")

        self.lbl_dPath = Label(self.master, text='Directory Path:', font=("Helvetica",16), fg='black')
        self.lbl_dPath.pack(side=TOP, pady=15)

        self.txt_dPath = Text(self.master, height=1.3, font=("Helvetica",14), fg='black', bg='white')
        self.txt_dPath.pack(padx=10, pady=20)

        self.btn_Search = Button(self.master, text='SEARCH', width=13, height=2, font=("Helvetica",14), fg='black', bg='lightgrey',command=dirSearch)
        self.btn_Search.pack(pady=20)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
