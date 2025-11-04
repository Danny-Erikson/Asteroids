# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# constants from constants.py
from constants import *
from player import Player


def main():
    print("Starting Asteroids!")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Lock fps so it does speed up or slow down with CPU speed
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Handler for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        player.draw(screen)
        pygame.display.flip()

        # Locks the game to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
