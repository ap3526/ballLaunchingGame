#Code created by Akash Patel CS-172-C Lab Section 069

import abc

class drawable(metaclass = abc.ABCMeta):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__visible = True
    #draw and getRect are abstract methods
    @abc.abstractmethod
    def draw(self, surface):
        pass
    @abc.abstractmethod
    def getRect(self):
        pass
    #returns location
    def getLoc(self):
        return (self.__x, self.__y)
    #returns x coordinate
    def getX(self):
        return self.__x
    #returns y coordinate
    def getY(self):
        return self.__y
    #can set location if needed
    def setLoc(self, p):
        self.__x = p[0]
        self.__y = p[1]
        
