import pygame
import random
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

    def split(self):
        # asteroid immdiately dies
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            spawn_angle = random.uniform(20, 50)
            asteroid1_velocity = pygame.Vector2(self.position.x, self.position.y).rotate(spawn_angle) * 1.2
            asteroid2_velocity = pygame.Vector2(self.position.x, self.position.y).rotate(-spawn_angle) / 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_velocity
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = asteroid2_velocity