from ursina import *

class Voxel(Button):
     def __init__(self, 
                  position=(0,0,0),
                  model='cube',
                  texture='white_cube',
                  mycolor=color.color(0, 0, random.uniform(.9, 1.0))
                ):
        super().__init__(parent=scene,
            position=position,
            model=model,
            origin_y=.5,
            texture=texture,
            color=mycolor,
            highlight_color=color.lime,
        )

class IndVoxel(Button):
     def __init__(self, 
                  position=(0,0,0),
                  model='cube',
                  texture='white_cube',
                  mycolor=color.color(0, 0, random.uniform(.9, 1.0))
                ):
        super().__init__(parent=scene,
            position=position,
            model=model,
            origin_y=.5,
            texture=texture,
            color=mycolor,
            highlight_color=color.lime,
        )