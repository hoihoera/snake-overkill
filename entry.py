import application, player, apple, layer, renderer
from properties import GRID_SIZE, RESOLUTION, FRAMERATE, TICKRATE 

class MainLayer(layer.Layer):
    def __init__(self):
        self._player = player.Player((GRID_SIZE[0]/2,GRID_SIZE[1]/2))
        self._apple = apple.Apple()

    def on_update(self):
        self._player.on_update()
        self._apple.on_update()
    
    def on_render(self):
        self._apple.on_render()
        self._player.on_render()
    
    def on_event(self):
        self._player.on_event()
        self._apple.on_event()
    
    def reset(self):
        del self._player
        del self._apple
        self.__init__()

application.Application.create(RESOLUTION[0],RESOLUTION[1],FRAMERATE,TICKRATE)
layers = [MainLayer()]
application.instance.layers.append(layers[0])
renderer.instance.layers.append(layers[0])
while(True):
    e = application.instance.run()
    if(e == 1): break
    layers[0].reset()