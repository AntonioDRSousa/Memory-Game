import tkinter as tk
from tkinter import Tk, ttk, Spinbox, Label
from Memory import *

class Game:
    def __init__(self):
        root = Tk()
        root.geometry("600x600")
        root.resizable(False,False)
        root.title("MEMORY")
        
        self.win1 = tk.Frame(root)
        self.win2 = tk.Frame(root)
        
        self.win1.pack(fill='both',expand=1)
        
        self.createMenu()
    
    def start(self,event):
        self.win1.forget()
        self.win2.pack(fill='both',expand=1)
        Memory(self.win2,self.win1,int(self.sp.get()))
        
    def createMenu(self):
        label = Label(self.win1,text='Number of Rows and Columns')
        self.sp = Spinbox(self.win1,justify=tk.CENTER,from_=2, to=10,state='readonly')
        button = ttk.Button(self.win1,text='start game')
        
        button.bind('<Button 1>',self.start)
        
        label.pack()
        self.sp.pack()
        button.pack()
        
        self.win1.mainloop()

if __name__=="__main__":
    Game()