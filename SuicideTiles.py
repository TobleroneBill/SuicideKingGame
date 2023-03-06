# Flyweight Pattern
#   General Block - Sprite, Solid, Kills, (aabb i guess)
#   Block types:
#       Rock - Solid
#       Wood - Solid, Can be set on fire (Spawns fire entity and deletes)
#       Spikes - Solid, kills
#       Water - not solid, slows movement and can kill after a long time (when breath runs out)
#       Hot Coals - Doesnt kill, but makes player jump like mario 64 in lava
import pygame
import AABB


# General block
class Block:
    def __init__(self,x,y,width,hight):
        self.aabb = AABB.AABB(x,y,width,hight)
        self.Texture = None
        self.Solid = True

class Rock(Block):
    def __init__(self,x,y,width,hight):
        super().__init__(x,y,width,hight)
        self.Texture = pygame.image.load('Assets\Blocks\Rock.png')