# Entities:
#   Main - AABB, VELOCITY, POSITION, COMMAND QUE, COLLISION CHECK, UPDATE
#   Player - Sprite
#   Enemy - Kill on collision
#       subTypes:
#           Joker - Patrol
#           Ace of spades - Fast X axis patrol
#           Jack of hearts - Still Jumper
#           Queen of Diamonds - Shoots Diamond Bullets
#               - Diamond Bullet (ace of diamonds) - Set movespeed + direction. Kills all entities on contact
#           King of clubs - Free x,y patrol movement
#   Extra Life
#   2-10 of diamonds - Adds score. Each type = number of diamonds
import AABB


class Entity:
    def __init__(self, x, y,width,height):
        self.x_ = x
        self.y_ = y
        self.xVel = 0
        self.yVel = 0
        self.COMMANDQUE = []
        self.HITBOX = AABB.AABB(x,y,width,height);

class Player(Entity):

    def PrintPos(self):
        print(f"x: {self.x_}, y: {self.y_}\nxVel{self.xVel}, yVel{self.yVel}")