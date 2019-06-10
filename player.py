from gameobject import *
from eventhandler import keys, getKey
from renderer import drawRect
from properties import checkCollision
import pygame
class Player(GameObject):
    def __init__(self, startPos):
        self.trueDir = 0
        self.inputDir = 0
        self.score = 0
        self.segments = []
        for i in range(3):
            self.segments.append((startPos[0],startPos[1]+i))
        self.length = len(self.segments)
    def on_update(self):
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
    def getHead(self): return self.segments[0]
    def eatApple(self):
        self.score += 1
        self.segments.append(self.tail)
    def on_event(self):
        if(getKey("w") or getKey("up")) and self.trueDir != 2:
           self.inputDir = 0   
        if(getKey("a") or getKey("left")) and self.trueDir != 3:
           self.inputDir = 1
        if(getKey("s") or getKey("down")) and self.trueDir != 0:
           self.inputDir = 2 
        if(getKey("d") or getKey("right")) and self.trueDir != 1:
           self.inputDir = 3
        
    def on_render(self):
        
        for s in self.segments:
            drawRect(s,(96,255,64))