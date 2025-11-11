# Used to draw sprites
import pygame

# used to create random velocities for split asteroids
import random

# Base class for game objects
from circleshape import CircleShape

# Constants
from constants import *

# Logger
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # If the asteroid is too small, don't split it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # send the two new asteroids in slightly different directions
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # build the two new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
