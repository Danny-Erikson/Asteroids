# Used to close the game
import sys

# Used to draw sprites
import pygame

# Used to get constants
from constants import *

# Import game objects
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

# Import logging functions
from logger import log_state, log_event


def main():
    print("Starting Asteroids!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Lock fps so it does speed up or slow down with CPU speed
    clock = pygame.time.Clock()
    dt = 0

    # Set up groups for sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Set player in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        log_state()

        # Handler for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable objects
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    break

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Locks the game to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
