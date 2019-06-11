import application, player, apple
from properties import GRID_SIZE, RESOLUTION, FRAMERATE, TICKRATE 


app = application.Application(RESOLUTION[0],RESOLUTION[1],FRAMERATE,TICKRATE)

app.gameObjects.append(apple.Apple())
app.gameObjects.append(player.Player((GRID_SIZE[0]/2,GRID_SIZE[1]/2)))

app.run()