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
import pygame

import AABB


class Entity:
    def __init__(self, x, y,width,height,LevelBlocks,screenref):
        self.Gravity = 0.1
        self.Grounded = False
        self.x_ = x
        self.y_ = y
        self.xVel = 0
        self.yVel = 0
        self.speed = 1
        self.COMMANDQUE = []
        self.HITBOX = AABB.AABB(x,y,width,height)
        # I think python makes this a refrence, but if not i will look into this
        self.LevelBlocks = LevelBlocks
        self.screen = screenref


    def M_LEFT(self):
        if self.xVel > -15:
            self.xVel -= self.speed

    def M_RIGHT(self):
        if self.xVel < 15:
            self.xVel += self.speed


    #TODO: Collision
    def CheckNearBlocks(self):
        CheckRange = 16
        CheckRect = pygame.Rect((self.x_ - CheckRange,self.y_ - CheckRange),(self.HITBOX.w + (CheckRange*2) ,self.HITBOX.h + (CheckRange*2)))
        pygame.draw.rect(self.screen,(0,255,255),CheckRect,5)
        #print(self.x_+self.HITBOX.w)
        count = 0
        nextx = self.x_ + self.xVel
        nexty = self.y_ + self.yVel
        for x in self.LevelBlocks:
            for Geo in x:
                # check if x and y is within check range (pointless to check every block
                # if left of entity
                #pygame.rect.Rect.colliderect()
                if Geo.aabb.rect.colliderect(CheckRect):
                    count+=1
                    #_________________X COLLISION_________________#
                    if self.HITBOX.CheckCollision(Geo.aabb):
                        # if this is negative (Usually positive because 0,0 starts from top left), move Left
                        print( nextx - Geo.aabb.x)
                        if nextx - Geo.aabb.x != 0:
                            if nextx - Geo.aabb.x > 0:
                                self.xVel = 0
                                self.x_ = Geo.aabb.x + Geo.aabb.w
                                print('left Collide')
                            else:
                                self.xVel = 0
                                self.x_ = Geo.aabb.x - self.HITBOX.w
                                print('Right Collide')

                        if nexty - Geo.aabb.y != 0:
                            if nexty - Geo.aabb.y > 0:
                                self.Grounded = True
                                self.yVel = 0
                                self.y_ = Geo.aabb.y - self.HITBOX.h
                                print('Bot Collide')

        if count == 0:
            print("no blocks in range")

    '''
    # OLD COLLISION METHOD (Initial Try)            
    # Left
    if Geo.aabb.x < self.x_:
        self.xVel -= self.xVel
        self.x_ = Geo.aabb.x + Geo.aabb.w
        print('left Collide')
    # Right
    if Geo.aabb.x > self.x_: # + self.HITBOX.w: # If its already collided, then we dont need to adjust for that
        self.xVel -= self.xVel
        self.x_ = Geo.aabb.x - self.HITBOX.w
        print('Right Collide')
    #_________________Y COLLISION_________________#
    if Geo.aabb.y > self.y_:    # Below
        self.yVel = 0
        self.y_ = Geo.aabb.y + Geo.aabb.h
        print('Bottom Collide')
    '''

    def Movement(self):
        # Check For Collision
        if self.yVel < 20 and not self.Grounded:
            pass
            self.yVel += self.Gravity
        scalar = 3
        pygame.draw.line(self.screen,(255,255,0),(self.x_,self.y_),(self.x_ + (self.xVel * self.HITBOX.w),self.y_ + (self.yVel * self.HITBOX.w)))
        self.CheckNearBlocks()

        # Update axis movement
        self.x_ += self.xVel
        self.y_ += self.yVel

        # Reduce xVelocity
        if self.xVel < 0:
            self.xVel += 0.5
        if self.xVel > 0:
            self.xVel -= 0.5



        self.HITBOX.UpdatePos(self.x_,self.y_)



class Player(Entity):

    def PrintPos(self):
        print(f"x: {self.x_}, y: {self.y_}\nxVel{self.xVel}, yVel{self.yVel}")

    def CheckNearEntities(self,EntityList):
        pass
