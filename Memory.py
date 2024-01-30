import tkinter as tk
from tkinter import Tk, ttk, messagebox
from random import choice
from Deck import *

class Memory:
    def __init__(self,win,win_back,nrc):
        self.win = win
        self.win_back = win_back
        
        self.dx = 25
        self.dy = 25
        self.size = 400
        
        self.canvas = tk.Canvas(self.win,width=self.size+self.dx*2,height=self.size+self.dy*2,bg="gray",highlightthickness=0)
        self.X0 , self.Y0 = 100 , 100
        self.canvas.place(x=self.X0-self.dx, y=self.Y0-self.dy)
        
        v = []
        for i in range(1,nrc+1):
            if ((nrc%i)==0):
                v.append(i)
        a = choice(v)
        b = nrc//a
        
        self.colors = ["cyan","red","blue","green1","magenta","yellow","orange","purple","green","red4"]
        self.shapes = ["circle1","circle2","square1","square2","square3"]
        self.colors = self.colors[:a]
        self.shapes = self.shapes[:b]
        
        
        self.deck, self.mx, self.my = (Deck(self.colors,self.shapes)).getMatrix()
        self.victory = (len(self.colors)*len(self.shapes))
        self.cselect = []

        self.sx = self.size/self.mx
        self.sy = self.size/self.my
        
        self.bind()
        
        self.draw()
        
        self.win.mainloop()
        
    def back(self):
        self.win.forget()
        self.win_back.pack(fill='both',expand=1)
    
    def move(self,x,y):
        def close(a0,a1):
            self.deck[a0[0]][a0[1]].open = False
            self.deck[a1[0]][a1[1]].open = False
            
        (self.deck[x][y]).open = True
        self.cselect.append((x,y))
        self.draw()
            
        if (len(self.cselect)==2):
            c0 , c1 = self.cselect[0] , self.cselect[1]
            if self.deck[c0[0]][c0[1]]==self.deck[c1[0]][c1[1]]:
                self.victory -= 1
                if self.victory==0:
                    messagebox.showinfo('Victory','You Win.')
                    self.back()
            else:
                close(c0,c1)
            self.cselect = []
        
        
    def getOrigin(self,event):
        x = int((event.x-self.dx)//self.sx)
        y = int((event.y-self.dy)//self.sy)

        if ( (x in range(self.mx)) and (y in range(self.my)) and (not((x,y) in self.cselect)) ):
            self.move(x,y)
                
    def bind(self):
        self.canvas.bind("<Button-1>",self.getOrigin)
        
    def draw(self):
        self.canvas.delete("all")
        for i in range(self.mx):
            for j in range(self.my):
                x0 = self.dx+i*self.sx
                x1 = x0+self.sx
                y0 = self.dy+j*self.sy
                y1 = y0+self.sy
                
                self.canvas.create_rectangle(x0,y0,x1,y1,fill="white")
                
                if (self.deck[i][j]).open:
                    a0 = x0+(self.sx//4)
                    a1 = x1-(self.sx//4)
                    b0 = y0+(self.sy//4)
                    b1 = y1-(self.sy//4)
                    ly = y0+((y1-y0)/2)
                    lx = x0+((x1-x0)/2)
                    (self.deck[i][j]).drawCard(self.canvas,a0,a1,b0,b1,lx,ly)