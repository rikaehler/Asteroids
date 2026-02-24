import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # type: ignore

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable) # type: ignore

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore

    AsteroidField.containers = (updatable) # type: ignore
    asteroidfield = AsteroidField()

    # Instantiate the player, automatically added to the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    # start game loop
    while True:
        log_state()

        # event game loop, exit loop when close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update all objects in group 'updatable'
        for obj in updatable:
            obj.update(dt)
        
        # collision detection between asteroid and player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        # collision detection between asteroid and bullet
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split() # removes from all Groups
                    shot.kill() # removes from all Groups

        # fill screen with solid black and draw screen
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
