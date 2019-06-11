import pygame,time,renderer
from properties import *

# application is a singleton (because there is only one application)
class Application:

    instance = None
    def __init__(self,width,height,framerate,tickrate):
        global instance ; instance = self
        pygame.init()
        pygame.font.init()
        self.framerate = framerate
        self.tickrate = tickrate
        self.createWindow(width,height)
        self.gameObjects = []
        self.running = True
    def run(self):
        dtime = 0
        while(self.running):
            dtime += 1/self.framerate
            if(dtime == 1/self.tickrate):
                dtime = 0
                self.on_update()
            self.on_render()
            self.on_event()
            time.sleep(1/self.framerate)

    def createWindow(self, width, height):
        renderer.screen = pygame.display.set_mode((width,height))        

    def on_render(self):
        renderer.screenBlank()
        for g in self.gameObjects: g.on_render()
        renderer.drawScreen()
    def on_update(self):
        for g in self.gameObjects: 
            g.on_update()               
    def on_event(self):
        for g in self.gameObjects: g.on_event()
        pygame.event.pump()

# entry point moved to entry.py (to seperate engine from client)