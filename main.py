# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    player.draw(screen)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Clear screen each frame
        screen.fill((0, 0, 0))
            
        for obj in updatable:
            # update the objects
            obj.update(dt)
        
        for obj in drawable:
            # draw the objects
            obj.draw(screen)

        #Flip the display
        pygame.display.flip()

        # Tick the clock
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()