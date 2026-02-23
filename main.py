import pygame
from constants import *
from logger import log_state
from player import Player

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

    # create groups to hold multiple updatable objects
    updatable =pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    # Instantiate the player, automatically added to the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)



    # start game loop
    while True:
        log_state()

        # event game loop, exit loop when close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #update all objects in group 'updatable'
        for obj in updatable:
            obj.update(dt)
            
        # fill screen with solid black and draw screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
