import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} ")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize pygame and get new instance of GUI window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create clock object and delta time
    clock = pygame.time.Clock()
    dt = 0

    #start game loop
    while True:
        log_state()

        # event game loop, exit loop when close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fill screen with solid black and refresh screen   
        screen.fill("black")
        pygame.display.flip
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
