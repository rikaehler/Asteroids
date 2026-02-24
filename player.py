import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        # initialize rotation attribute
        self.rotation = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # type: ignore
        b = self.position - forward * self.radius - right # type: ignore
        c = self.position - forward * self.radius + right # type: ignore
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            LINE_WIDTH
        )

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOOT_RADIUS)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        new_shot.velocity = velocity * PLAYER_SHOT_SPEED
    
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # player rotation based on delta time
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(+dt)
        if keys[pygame.K_w]:
            self.move(+dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()