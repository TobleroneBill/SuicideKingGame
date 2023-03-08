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
import sys

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
        if self.xVel > -12:
            self.xVel -= self.speed

    def M_RIGHT(self):
        if self.xVel < 12:
            self.xVel += self.speed


    #TODO: Collision
    def CheckNearBlocks(self):
        # number of Geometry Nodes Collided with
        count = 0
        # new position to check
        nextx = self.x_ + self.xVel
        nexty = self.y_ + self.yVel
        NextRect = pygame.Rect((nextx,nexty),(self.HITBOX.w,self.HITBOX.h))

        #deubg visualisation
        pygame.draw.rect(self.screen,(0,255,255),NextRect,5)
        pygame.draw.line(self.screen,(255,255,255),(self.x_,self.y_),(nextx,nexty ),10)

        # List of collided Tiles
        colliders = []
        for x in self.LevelBlocks:
            for Geo in x:
                # If next position collides with Level data
                if Geo.aabb.rect.colliderect(NextRect):
                    colliders.append(Geo)
                    count += 1

        if colliders.__len__() != 0:
            print("#################COLLISION CHECK################")
            print("--------------------------------")
            print(f'NextPos X: {NextRect.x}, Y: {NextRect.y}')
            print("--------------------------------")
            for no,tile in enumerate(colliders):
                newY = NextRect.y - tile.aabb.y
                newX = NextRect.x - tile.aabb.x

                print(f'CollideTile no {no} X: {tile.aabb.x}, Y: {tile.aabb.y}')
                print(f'''ABS of of positions:
                      X: {abs(newX)}
                      y: {abs(newY)}''')
                # if x intercept is less than y intercept, x takes precidence (because it has the shallow axis)
                if abs(newX) > abs(newY):
                    if newX > 0:
                        self.x_ = tile.aabb.x + tile.aabb.w + (-self.xVel)
                        self.xVel = 0
                        print('left Collide')
                    else:
                        pass
                        self.x_ = tile.aabb.x - self.HITBOX.w - (+self.xVel)
                        self.xVel = 0
                        print('Right Collide')
                # Y precidence
                else:
                    # TODO: Sliding isnt supported
                    if newY < 0:
                        self.y_ = tile.aabb.y - self.HITBOX.w - self.yVel
                        self.yVel = 0
                        self.Grounded = True
                        print('Bot Collide')
                    else:
                        self.y_ = tile.aabb.y + tile.aabb.w
                        self.yVel = -self.yVel
                        print('Top Collide')

            #print(colliders)
    '''
    # Another Failed Attempt #
        # Get the closest axis positions of all the detected colliders 
        minX = None
        minY = None
        if colliders.__len__() > 1:
            # Find the closest Collider positions
            for Geo in colliders:
                if minX is None and minY is None:
                    minX = Geo.aabb.x
                    minY = Geo.aabb.y
                    continue

                # This will only run if number of colliders is greater than 1
                # get the difference of the next rect and the minx, and the geo x. Whichever one is smaller will be minX
                if Geo.aabb.x - NextRect.x < minX - NextRect.x:
                    minX = Geo.aabb.x

                # Same as above
                if Geo.aabb.Y - NextRect.y < minY - NextRect.y:
                    minY = Geo.aabb.y
        else:
            minX = colliders[0].aabb.x
            minY = colliders[0].aabb.y

        #_________________COLLISION RESPONSE_________________#
            
            # With the saved knowledge of the closest X and Y positions to the NextPosition, we know what Dir to push
            # The player (actually we dont lol)
            
            
        xintersect = nextx - closestX
        yintersect = nexty - closestY

        # if this is negative (Usually positive but 0,0 starts from top left), move Left
        # if y is smaller than x, then we need to collide with y axis because it is closer than than the x

        if xintersect > 0:
            self.xVel = 0
            self.x_ = Geo.aabb.x + Geo.aabb.w
            print('left Collide')
        else:
            self.xVel = 0
            self.x_ = Geo.aabb.x - self.HITBOX.w
            print('Right Collide')
            '''

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
            self.yVel += self.Gravity
            pass

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
