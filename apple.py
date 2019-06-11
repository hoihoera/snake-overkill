from gameobject import *
from properties import GRID_IMAX
from renderer import drawRect
import random
class Apple(GameObject):
    # ik heb hier een singleton van gemaakt. als de apple
    # wordt aangemaakt, wordt een verwijzing daarvan in 
    # instance opgeslagen, waardoor andere scripts de data
    # makkelijk kunnen bereiken.
    instance = None
    def __init__(self):
        global instance
        self.pos = (0,0) 
        self.reset()
        self.blinkcount = 0
        self.normalColor = (255,48,80)
        self.blinkColor = (255,192,48)
        self.color = self.normalColor
        instance = self
    def on_update(self):
        if(self.blinkcount == 4):
            self.color = self.blinkColor
            self.blinkcount = 0
        else: self.color = self.normalColor
        self.blinkcount += 1
    def reset(self):
        self.pos = (random.randint(0,GRID_IMAX[0]),random.randint(0,GRID_IMAX[1]))
    def on_render(self):
        drawRect(self.pos,self.color)