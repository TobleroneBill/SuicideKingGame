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
        self.Gravity = 1
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
        for x in self.LevelBlocks:
            for y in x:

                # check if x and y is within check range (pointless to check every block
                # if left of entity
                #pygame.rect.Rect.colliderect()
                if y.aabb.rect.colliderect(CheckRect):
                    count+=1
                    #_________________X COLLISION_________________#
                    if self.HITBOX.CheckCollision(y.aabb) and y.aabb.x < self.x_:   #Left
                        self.xVel = 0
                        self.x_ = y.aabb.x+ y.aabb.w
                        print('left Collide')
                        return
                    if self.HITBOX.CheckCollision(y.aabb):      # Right
                        self.xVel = 0
                        self.x_ = y.aabb.x - self.HITBOX.w
                        print('Right Collide')
                        return
                    #_________________Y COLLISION_________________#
                    if self.HITBOX.CheckCollision(y.aabb)  and y.aabb.y > self.y_:      # Down
                        self.yVel = 0
                        self.x_ = y.aabb.y - self.HITBOX.h
                        print('BotCOllide')
                        return
                    if self.HITBOX.CheckCollision(y.aabb):      # Up
                        self.xVel = 0
                        self.x_ = y.aabb.x - self.HITBOX.w
                        print('Right Collide')
                        return

       # print(count)
                #if y.aabb.y > self.y_ - CheckRange or y.aabb.y > self.y_ - CheckRange:
                #    if self.HITBOX.CheckCollision(y.aabb):
                #        print('Y Collide')


    def Movement(self):
        # Check For Collision
        if self.yVel < 20:
            self.yVel += self.Gravity
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
