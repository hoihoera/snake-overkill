import pygame
keys = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT, 
    "right": pygame.K_RIGHT, 
    "w": pygame.K_w,
    "a": pygame.K_a,
    "s": pygame.K_s,
    "d": pygame.K_d,
    "esc": pygame.K_ESCAPE
    }

def getKey(key):
    out = pygame.key.get_pressed()[keys[key]]
    pygame.event.pump()
    return out
