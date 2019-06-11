import pygame
from properties import worldToScreen, GRID_SCALE, GRID_SIZE
screen = None

def drawScreen(): pygame.display.flip()

def drawRect(pos: (int,int), color: (int,int,int)):
    screenPos = worldToScreen(pos)
    pygame.draw.rect(screen,color,pygame.Rect(screenPos[0],screenPos[1],GRID_SCALE,GRID_SCALE))

def screenBlank ():
    screen.fill((80,128,200))
    pygame.draw.rect(screen,(40,48,64),pygame.Rect(
        GRID_SCALE,GRID_SCALE,GRID_SIZE[0]*GRID_SCALE,GRID_SIZE[1]*GRID_SCALE))