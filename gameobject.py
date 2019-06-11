# interface from which all game objects should derive
class GameObject:

    def __init__(self): # constructor
        pass
    
    def on_update(self): # runs every gametick
        pass

    def on_event(self): # runs every frame (event polling)
        pass

    def on_render(self): # runs every frame (rendering)
        pass
