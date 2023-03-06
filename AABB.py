# General AABB
import pygame


class AABB:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x,y,w,h)

    def UpdatePos(self,newx,newy):
        self.x = newx
        self.y = newy
        self.rect.y = newy
        self.rect.x = newx

    def DrawHitBox(self,screen):
        pygame.draw.rect(screen,(255,0,0),self.rect,5)

    def CheckCollision(self,otherRect):
        # pygame has this built in, but is just:
        # if any of the points of the rect are inside of the collider, then true else false
        return self.rect.colliderect(otherRect)