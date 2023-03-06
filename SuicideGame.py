# Classes:
#   GM
#   CONTROLLER
#   COMMAND
import pygame

import SuicideLevel


#______________________Game Manager______________________#
class GameManager:
    # Pygame
    pygame.init()
    WIDTH,HEIGHT = 800,800
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    CLOCK = pygame.time.Clock()
    FPS = 60
    LEVEL = SuicideLevel.Level(None)  # Will update level during level transitions

    @staticmethod
    def Main():
        gaming = True
        while gaming:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    gaming = False
            GameManager.Update()
    @staticmethod
    def Update():
        GameManager.LEVEL.DrawDebug(GameManager.SCREEN)
        GameManager.CLOCK.tick(GameManager.FPS) # 60FPS
        pygame.display.update()
        #print(help(C_Jump))


#______________________Command and input______________________#
# Check for keypresses
# Execute commands on player
# Store command Que
class Input:
    def __init__(self):
        self.LeftKey = pygame.K_LEFT
        self.RightKey = pygame.K_RIGHT
        self.JumpKey = pygame.K_SPACE
        self.inputArr = []  #Stores input each Tick, to be used in replay
    # Check for keypress
    def GetInput(self,CurrentEvent):
        pass
class Command:
    def execute(self):
        pass

# All commands inherit main command
class C_Jump(Command):
    pass

class C_MoveLeft(Command):
    pass

class C_MoveRight(Command):
    pass
