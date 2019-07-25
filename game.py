#Code created by Akash Patel CS-172-C Lab Section 069

from drawable import *
from ball import *
from block import *
from text import *
import pygame

pygame.init()
surface = pygame.display.set_mode((500, 500))
white = (255, 255, 255)
black = (0, 0, 0)

#intersect function from hw4 prompt
def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y):
        return True
    else:
        return False


fpsClock = pygame.time.Clock()
#instantiate variables
dt = 0.1
g = 6.67
r = 0.7
eta = 0.5
xInit = 0
yInit = 0
xEnd = 0
yEnd = 0
xv = 0
yv = 0
x_fin = 0
y_fin = 0
points = 0
begin = True
blocks = []
#instantiate 9 blocks
blok = block(400, 380)
blok2 = block(380, 380)
blok3 = block(360, 380)
blok4 = block(400, 360)
blok5 = block(380, 360)
blok6 = block(360, 360)
blok7 = block(400, 340)
blok8 = block(380, 340)
blok9 = block(360, 340)
#add blocks to list of blocks
blocks.extend((blok, blok2, blok3, blok4, blok5, blok6, blok7, blok8, blok9))
while(True):
    #for first iteration, set up game screen
    if begin:
        surface.fill(white)
        pygame.draw.line(surface, black, [0,400], [500, 400], 1)
        for contents in blocks:
            contents.draw(surface)
        ba = ball(20, 392)
        ba.draw(surface)
        score = text("Score: " + str(points))
        score.draw(surface)
        begin = False
    surface.fill(white)
    pygame.draw.line(surface, black, [0,400], [500, 400], 1)
    #loop through blocks list and draw them
    for contents in blocks:
        contents.draw(surface)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
        #user is only able to modify ball if it is in starting position
        if(ba.getLoc()[0]==20 and ba.getLoc()[1]==392):
            #record location coordinates when user clicks and releases mouse
            if(event.type == pygame.MOUSEBUTTONDOWN):
                xInit, yInit = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONUP):
                xEnd, yEnd = pygame.mouse.get_pos()
                xv = xInit - xEnd
                yv = yInit - yEnd
    #if bottom of ball is about to go under the line, make it bounce
    if(ba.getLoc()[1] > 391): 
        yv = -r * yv
        xv = eta * xv
    #else apply gravity
    else:
        yv = yv - g * dt
    #calculate final velocities including the delta time variable
    x_fin = dt * xv
    y_fin = dt * yv


    #add the new velocities to current location
    location = ba.getLoc()
    bounce = location[0] + int(x_fin)
    high = location[1] - int(y_fin)
    #ball cannot go below the line. 392 because of the radius of the circle
    if(high > 393):
        high = 392
    newValues = [bounce, high]
    #set location of ball to new coordinates
    ba.setLoc(newValues)
    ba.draw(surface)
    #loop through blocks and check if each intersect with the ball
    #if they do, set the block's visible to false
    for coll in blocks:
        if intersect(ba.getRect(), coll.getRect()):
            if(coll.visible is True):
                coll.visible = False
                points = points + 10
    if points == 90:
        score = text("Score: " + str(points) + " You win! Q to quit")
    else:
        score = text("Score: " + str(points))
    score.draw(surface)
    #if the ball goes off the screen or stops moving, restart
    if((ba.getX()<0 or ba.getX()>500) or (int(x_fin) == 0 and int(y_fin) == 0)):
        begin = True
        xv = 0
        yv = 0

    


    pygame.display.update()
    fpsClock.tick(60)
    


