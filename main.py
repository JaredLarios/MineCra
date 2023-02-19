'''
Disclaimer: This solution is not scalable for creating a big world.
Creating a game like Minecraft requires specialized knowledge and is not as easy
to make as it looks.
You'll have to do some sort of chunking of the world and generate a combined mesh
instead of separate blocks if you want it to run fast. You can use the Mesh class for this.
You can then use blocks with colliders like in this example in a small area
around the player so you can interact with the world.
'''

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from Game.Services.ursina_service import Voxel
from Game.materials import Materials
from Game.map import Landscape


app = Ursina()
materials = Materials()
landscape = Landscape()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.

# class Voxel(Button):
#     def __init__(self, position=(0,0,0)):
#         super().__init__(parent=scene,
#             position=position,
#             model='cube',
#             origin_y=.5,
#             texture='white_cube',
#             color=color.color(0, 0, random.uniform(.9, 1.0)),
#             highlight_color=color.lime,
#        )

# for z in range(8):
#     for x in range(8):
#         voxel = materials.grass(position=(x,0,z))
#         voxel = materials.crete_object()

landscape.ground(x=25, y=25, z=3)
for x in range(8):
    landscape.trees()


def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)


player = FirstPersonController()
app.run()