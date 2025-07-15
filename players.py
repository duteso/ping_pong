import pygame
from define import *

class Player():
    x=0
    y=0
    colour=""
    
    def __init__(self, colour, x, y)->None:
        self.x=x
        self.y=y
        self.colour=colour
        self.score = 0
        
    def show(self, surface):
        pygame.draw.rect(surface,self.colour, (self.x,self.y,p_width,p_height),width=0)
    
    def moveUP(self):
        self.y-= p_speed
        if self.y<0:
            self.y=0
            
    def moveDown(self):
        self.y+=p_speed
        if self.y > WINDOW_HEIGHT - p_height:
            self.y = WINDOW_HEIGHT - p_height