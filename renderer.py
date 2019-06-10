import pygame
from properties import worldToScreen, GRID_SCALE
screen = None

def drawScreen(): pygame.display.flip()

def drawRect(pos: (int,int), color: (int,int,int)):
    screenPos = worldToScreen(pos)
    pygame.draw.rect(screen,color,pygame.Rect(screenPos[0],screenPos[1],GRID_SCALE,GRID_SCALE))
