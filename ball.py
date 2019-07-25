#Code created by Akash Patel CS-172-C Lab Section 069

from drawable import *
import pygame

class ball(drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__visible = True
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), [self.getX(), self.getY()], 8 )
    #returns rectangle around ball  
    def getRect(self):
        return pygame.Rect(self.getX() - 8, self.getY() - 8, 16, 16)
    #returns location of ball
    def getLoc(self):
        return (self.getX(), self.getY())
    

    
        
    