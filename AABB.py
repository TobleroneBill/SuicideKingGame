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

    def CheckCollision(self,otherRect):
        pass