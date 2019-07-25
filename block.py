#Code created by Akash Patel CS-172-C Lab Section 069

from drawable import *
import pygame

class block(drawable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.visible = True
    
    def draw(self, surface):
        #only draw if visible is true
        #draws a filled rectangle then a black rectangle around it
        if(self.visible is True):
            surface.fill((0,0,255), pygame.draw.rect(surface, (255, 255, 255), (self.getX(), self.getY(), 20, 20)))
            pygame.draw.rect(surface, (0, 0, 0), (self.getX(), self.getY(), 20, 20), 1)
        else:
            pass
    def getRect(self):
        return pygame.Rect(self.getX(), self.getY(), 20, 20)
    #changes visible 
    def changeVisible(self):
        if self.__visible is True:
            self.__visible = False
        else:
            self.__visible = True