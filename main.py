# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# constants from constants.py
import constants as const


def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
