# Classes:
#   GM
#   CONTROLLER
#   COMMAND
import pygame
import SuicideEntities
import SuicideLevel


#______________________Game Manager______________________#
class GameManager:
    # Pygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    FPS = 60
    LEVEL = SuicideLevel.Level(None)  # Will update level during level transitions
    WIDTH,HEIGHT = 800,800
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    PLAYER = SuicideEntities.Player(400,400,32,32,LEVEL.levelData,SCREEN)
    @staticmethod
    def Main():
        INPUTMANAGER = Input(GameManager.PLAYER)
        gaming = True
        while gaming:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    gaming = False
            INPUTMANAGER.GetInput(event)
            GameManager.Update()

    @staticmethod
    def Update():
        GameManager.SCREEN.fill((0,0,0))
        GameManager.PLAYER.HITBOX.DrawHitBox(GameManager.SCREEN)
        GameManager.PLAYER.Movement()
        #GameManager.PLAYER.PrintPos()
        GameManager.LEVEL.DrawDebug(GameManager.SCREEN)
        GameManager.CLOCK.tick(GameManager.FPS) # 60FPS

        pygame.display.update()
        #print(help(C_Jump))


#______________________Command and input______________________#
# Check for keypresses
# Execute commands on player
# Store command Que
class Input:
    def __init__(self,Actor):
        self.LeftKey = pygame.K_LEFT
        self.RightKey = pygame.K_RIGHT
        self.JumpKey = pygame.K_SPACE
        self.InputArr = []  # Stores input each Tick, to be used in replay
        self.Actor = Actor  # Player Reference

    # Check for keypress
    def GetInput(self,CurrentEvent):
        if pygame.key.get_pressed()[self.LeftKey]:
            self.Actor.M_LEFT()
        if pygame.key.get_pressed()[self.RightKey]:
            self.Actor.M_RIGHT()

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
