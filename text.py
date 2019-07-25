#Code created by Akash Patel CS-172-C Lab Section 069

from drawable import  *
import pygame

class text(drawable):
    def __init__(self, message, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x,y)
        self.__x = x
        self.__y = y
        self.message = message
        self.visible = True
        fontObj = pygame.font.Font("freesansbold.ttf", 32)
        self.surface = fontObj.render(message, True, color)
        
    def draw(self, surface):
        surface.blit(self.surface, self.getLoc())
        
    
    def getRect():
        pass