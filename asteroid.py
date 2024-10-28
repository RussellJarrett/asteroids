import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            [self.position.x, self.position.y], 
            self.radius)

    def update(self, dt):
        self.position += self.velocity * dt