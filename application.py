import pygame,time,renderer,gameobject
from properties import *

# application is a singleton (because there is only one application)
class Application:

    instance = None
    @staticmethod
    def create(width,height,framerate,tickrate):
        global instance ; instance = Application(width,height,framerate,tickrate)

    def __init__(self,width,height,framerate,tickrate):
        self.framerate = framerate
        self.tickrate = tickrate
        self.layers = []
        self.running = True
        self.exeTime = 0
        
        pygame.init()
        pygame.font.init()
        self.coreFont = pygame.font.SysFont("arial",24,bold=True)

        renderer.Renderer.create()

        renderer.instance.screen.blit(self.coreFont.render("Hi :)",True,(48,255,96)),(10,10))
        renderer.instance.screen.blit(self.coreFont.render("Open Leesmij.txt",True,(48,255,96)),(10,40))
        renderer.instance.drawScreen()
        time.sleep(3)

    def run(self):
        clock = pygame.time.Clock()
        dtime = 0
        self.running = True
        while(self.running):
            dtime += 1/self.framerate           
            if(dtime >= 1/self.tickrate):                              
                dtime = 0
                self.on_update()
            renderer.instance.render()
            self.on_event()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: return 1
            time.sleep(1/self.framerate) 
        time.sleep(0.6)
        return 0
    def on_update(self):
        for l in self.layers: l.on_update()               
    def on_event(self):
        for l in self.layers: l.on_event()
        pygame.event.pump()

# entry point moved to entry.py (to seperate engine from client)