from gameobject import *
from eventhandler import keys, getKey
import renderer
from properties import checkCollision, GRID_IMAX
import apple
import application
import time
class Player(GameObject):
    # Constructor
    def __init__(self, startPos):
        self.alive = True # player starts alive (ofc)
        self.trueDir = 0 # the direction the player is moving in (updates every game tick)
        self.inputDir = 0 # the direction changed by input polling (updates every frame)
        self.score = 0 # the score of the player (length - 3)
        self.color = (96,255,64)
        self.deathColor = (192,48,80)
        self.segments = [] # the body of the snake
        for i in range(3):
            self.segments.append((startPos[0],startPos[1]+i))
        self.length = len(self.segments)
    # inherited from GameObject
    def on_update(self):
        if(not self.alive): return
        self.trueDir = self.inputDir
        for i in range(self.length-1,0,-1):
            self.segments[i] = self.segments[i-1]
        self.tail = self.segments[self.length-1]
        if(self.trueDir == 0):
            self.segments[0] = (self.segments[0][0], self.segments[0][1]-1)
        if(self.trueDir == 1):
            self.segments[0] = (self.segments[0][0]-1, self.segments[0][1])
        if(self.trueDir == 2):
            self.segments[0] = (self.segments[0][0], self.segments[0][1]+1)
        if(self.trueDir == 3):
            self.segments[0] = (self.segments[0][0]+1, self.segments[0][1])
        if(apple.instance.pos == self.segments[0]):
            self.eatApple()
            apple.instance.reset()
        for i in range(1,self.length):
            if(self.segments[0] == self.segments[i]): self.alive = False ; break
        if self.segments[0][0] < 0 or self.segments[0][0] > GRID_IMAX[0] or self.segments[0][1] < 0 or self.segments[0][1] > GRID_IMAX[1]: self.alive = False
        if not self.alive: 
            application.instance.running = False 
            self.color = self.deathColor    
    def getHead(self): return self.segments[0]
    
    def eatApple(self): 
        self.score += 1
        self.segments.append(self.tail)
        self.length += 1
    # inherited from GameObject
    def on_event(self):
        if(getKey("w") or getKey("up")) and self.trueDir != 2:
           self.inputDir = 0   
        if(getKey("a") or getKey("left")) and self.trueDir != 3:
           self.inputDir = 1
        if(getKey("s") or getKey("down")) and self.trueDir != 0:
           self.inputDir = 2 
        if(getKey("d") or getKey("right")) and self.trueDir != 1:
           self.inputDir = 3
    # inherited from GameObject
    def on_render(self):
        if(self.alive):
            for s in self.segments: renderer.instance.drawRect(s,self.color)
        else:
            for i in range(1,self.length):
                renderer.instance.drawRect(self.segments[i],self.color)