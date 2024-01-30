from random import shuffle
from Card import *

class Deck:
    def __init__(self,colors,shapes):
    
        self.colors = colors
        self.shapes = shapes
        
        self.deck = []
        for i in colors:
            for j in shapes:
                self.deck.append(Card(i,j))
                self.deck.append(Card(i,j))
                
        shuffle(self.deck)
        self.getMatrix()
        
    def getMatrix(self):
        if len(self.colors)>len(self.shapes):
            m=len(self.colors)
            n=2*len(self.shapes)
        else:
            m=len(self.shapes)
            n=2*len(self.colors)
        
        mat = [None]*m
        for i in range(m):
            mat[i] = [None]*n
            for j in range(n):
                mat[i][j] = self.deck[i*n+j]
                
        return mat, m, n  