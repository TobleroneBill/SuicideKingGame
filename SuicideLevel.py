# Maybe should be Json with the level data, but just holds each levels data
# Levels are 25x25 square tiles with a size of 32
# (One screen big, so shouldnt bee too huge)

# aiming for around 52 levels to be thematically accurate

# Level holds:
#   Block Data
#   Entity Data
#   High Score + Fastest Time
#   Completed Check (For level selection screen)
import json

import pygame

import SuicideTiles


class Level:
    # Each level is 32x25
    blocksize = 32
    LevelSize = 800 # num of pixels
    resolution = int(LevelSize/blocksize)   # Res of 25

    def __init__(self,levelJSON):
        self.levelData = TestLevel()

    def GenerateDebugLevel(self):
        print(Level.resolution)
        level = []
        for x in range(Level.resolution):
            col = []
            for y in range(Level.resolution):
                Rect = pygame.Rect(x * Level.blocksize, y * Level.blocksize, Level.blocksize,Level.blocksize)
                col.append(Rect)
            level.append(col)
        return level

    def DrawDebug(self,screen):
        color = (255,255,255)
        # 2d array
        for x in self.levelData:
            # each array in x
            for y in x:
                screen.blit(y.Texture,(y.aabb.x,y.aabb.y))

def TestLevel():
    level = []
    for x in range(Level.resolution):
        col = []
        for y in range(Level.resolution):
            # Edges
            if y == 0 or y == 24 or x == 0 or x == 24:
                Block = SuicideTiles.Rock(x*Level.blocksize,y*Level.blocksize,Level.blocksize,Level.blocksize)
                col.append(Block)
        level.append(col)
    return level

