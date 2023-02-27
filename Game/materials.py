from ursina import *
from Game.Services.ursina_service import Voxel, IndVoxel
class Materials():
    # Materials made by entities of ursina
    
        def __init__(self):
            # init the material things
            self._position = (0,0,0)
            self._model ='cube'
            self._texture = 'white_cube'
            self._color = color.color(0, 0, random.uniform(.9, 1.0))
            self._x = 0
            self._y = 0
            self._z = 0

            

        def grass(self, position):
            # entity made of grass
            self._position = position
            self._texture = "grass"
            self._color = color.color(0, 0, random.uniform(.9, 1.0))
                

        def earth(self, position):
            # entity made of ground
            self._position = position
            self._texture = "grass"
            self._color = color.brown

        def wood(self, position):
            # entity made of wood
            self._position = position
            self._texture = "grass"
            self._color = color.rgb(185, 82, 82)

        def glass(self):
            # entity made of glass
            pass

        def leaves(self):
            # entity made of leaves
            pass

        def rocks(self, position):
            self._position = position
            self._texture = "grass_tintable"
            self._color = color.gray


        def create_object(self):
            return Voxel(
                  position=self._position,
                  model=self._model,
                  texture=self._texture,
                  mycolor=self._color
            )
        
        def create_indestructible_object(self):
            return IndVoxel(
                  position=self._position,
                  model=self._model,
                  texture=self._texture,
                  mycolor=self._color
            ) 
        
