class Card:
    def __init__(self,color,shape):
        self.color = color
        self.shape = shape
        self.open = False
        
    def __eq__(self, c):
        return ((self.color==c.color)and(self.shape==c.shape))
        
    def getTuple(self):
        return (self.color,self.shape)
        
    def turn(self):
        self.open = not self.open
        
    def drawCard(self,canvas,a0,a1,b0,b1,lx,ly):
        if self.shape=="circle1":
            canvas.create_oval(a0,b0,a1,b1, fill = self.color)
        elif self.shape=="circle2":
            canvas.create_oval(a0,b0,a1,b1, outline = self.color, fill = "white",width = 2)
        elif self.shape=="square1":
            canvas.create_rectangle(a0,b0,a1,b1, fill = self.color)
        elif self.shape=="square2":
            canvas.create_rectangle(a0,b0,a1,b1, outline = self.color, fill = "white",width = 2)
        else:
            canvas.create_line(a0,ly,lx,b0,fill=self.color,width=2)
            canvas.create_line(a0,ly,lx,b1,fill=self.color,width=2)
            canvas.create_line(lx,b0,a1,ly,fill=self.color,width=2)
            canvas.create_line(lx,b1,a1,ly,fill=self.color,width=2)