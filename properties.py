GRID_SIZE = (32,32)
GRID_IMAX = (GRID_SIZE[0]-1,GRID_SIZE[1]-1)
GRID_SCALE = 16
RESOLUTION = ((GRID_SIZE[0]+2)*GRID_SCALE,(GRID_SIZE[1]+2)*GRID_SCALE)
FRAMERATE = 30
TICKRATE = 10

def worldToScreen(pos):
    return ((pos[0]+1)*GRID_SCALE,(pos[1]+1)*GRID_SCALE)

def checkCollision(p1,p2):
    return p1[0]==p2[1] and p1[1] == p2[1]

def validate():
    if(GRID_SIZE[0] < 6 or GRID_SIZE[1] < 6):
        return 1
    if(GRID_SIZE[0] % 1 != 0 or GRID_SIZE[1] % 1 != 0):
        return 2
    if(GRID_SCALE < 1 or GRID_SCALE % 1 != 0):
        return 3
    if(FRAMERATE % TICKRATE != 0):
        return 4
    return 0

FPT = FRAMERATE/TICKRATE