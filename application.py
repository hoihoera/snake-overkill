import pygame,time,renderer
from properties import *
from player import *
from apple import *
class Application:

    def __init__(self,width,height,framerate,fpt):
        pygame.init()
        pygame.font.init()
        self.framerate = framerate
        self.framespertick = fpt
        self.createWindow(width,height)
        self.gameObjects = []
    
    def run(self):
        fcount = 0
        while(True):
            fcount += 1
            if(fcount == self.framespertick):
                fcount = 0
                self.on_update()
            
            self.on_render()
            self.on_event()
            time.sleep(1/self.framerate)


    def createWindow(self, width, height):
        renderer.screen = pygame.display.set_mode((width,height))        

    def on_render(self):
        renderer.screen.fill((80,128,200))
        pygame.draw.rect(renderer.screen,(40,48,64),pygame.Rect(GRID_SCALE,GRID_SCALE,GRID_SIZE[0]*GRID_SCALE,GRID_SIZE[1]*GRID_SCALE))
        for g in self.gameObjects: g.on_render()
        renderer.drawScreen()
    def on_update(self):
        for g in self.gameObjects: 
            g.on_update()
            if(isinstance(g,Player)):
                for i in range(1,g.length):
                    if checkCollision(g.getHead(),g.segments[i]):
                        
                
    def on_event(self):
        for g in self.gameObjects: g.on_event()



a = Application(RESOLUTION[0],RESOLUTION[1],FRAMERATE,FPT)
a.gameObjects.append(Player((GRID_SIZE[0]/2,GRID_SIZE[1]/2)))
a.gameObjects.append(Apple())
a.run()