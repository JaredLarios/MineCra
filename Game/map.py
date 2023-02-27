from Game.materials import Materials
import random
class Landscape(Materials):

            def ground(self, x, y, z):
                    # choosse tghe length and the width and hight
                    # of the ground
                    self._x = x
                    self._y = y
                    self._z = z

                    for height in range(z):
                        for width in range(y):
                            for length in range(x):
                                if height == z-1:
                                    voxel = self.grass(position=(length,height,width))
                                    voxel = self.create_object()

                                elif  height == z-2: 
                                    voxel = self.earth(position=(length,height,width))
                                    voxel = self.create_object()
                                
                                elif height == z-3:
                                    voxel = self.rocks(position=(length,height,width))
                                    voxel = self.create_indestructible_object()

            def trees(self):
                    #add randomly an amount and of trees and the program choose
                    # where to plant it
                    z, x, y = random.randrange(self._z,5), random.randrange(1,self._x-1), random.randrange(1,self._y-1)

                    for height in range(z+3):
                        for width in range(self._y):
                            for length in range(self._x):
                                if width == y and length == x:
                                    voxel = self.wood(position=(length,height,width))
                                    voxel = self.create_object()

                     
                    for height in range(z+6):
                        for width in range(self._y):
                            for length in range(self._x):
                                 if (width >= y-1 and width <= y+1)  and (length >= x-1 and length <= x+1) and height > z:
                                    voxel = self.grass(position=(length,height,width))
                                    voxel = self.create_object()



