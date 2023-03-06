# This is a game made for testing out the flyweight and command programming patterns in a way that has a
# fun use case.
#
# Game Features:
#   - Player objective is to KMS ASAP
#   - Is a time trial to see how fast the player can KMS
#   - Using the control system to record inputs + execute
#   - input recording is then used to supermeatboy/doom style see how the game has played out when finished
#   - Grid Based Level system (perhaps using my old level editor
#   - Grid Pieces are Tiles, using flyweight as an optimization method + cool stuff
import pygame

if __name__ == "__main__":
    pygame.init()
    WIDTH,HEIGHT = 960,540
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    gaming = True

    while gaming:
        for events in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_ESCAPE] or events.type == pygame.QUIT:
                gaming = False

    print("Game End")