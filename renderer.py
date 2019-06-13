import pygame
from properties import worldToScreen, GRID_SCALE, GRID_SIZE, RESOLUTION
from layer import Layer
instance = None
class Renderer:

    @staticmethod
    def create():
        global instance ; instance = Renderer()

    def __init__(self):
        self.layers = []
        self._screen = pygame.display.set_mode((RESOLUTION[0], RESOLUTION[1]))

    def render(self):
        self.screenBlank()
        for l in self.layers:
            l.on_render()
        self.drawScreen()
        
    @property
    def screen(self): return self._screen
        
    def drawRect(self, pos: (int, int), color: (int, int, int)):
        screenPos = worldToScreen(pos)
        pygame.draw.rect(self._screen, color, pygame.Rect(screenPos[0], screenPos[1], GRID_SCALE, GRID_SCALE))

    def drawScreen(self): pygame.display.flip() 

    def screenBlank (self):
        self._screen.fill((80, 128, 200))
        pygame.draw.rect(self._screen, (40, 48, 64), pygame.Rect( 
            GRID_SCALE, GRID_SCALE, GRID_SIZE[0] * GRID_SCALE, GRID_SIZE[1] * GRID_SCALE))