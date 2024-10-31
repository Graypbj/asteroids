import pygame
from constants import *
from player import Player

def main():
    # Initialize game and add constants for screen size and clock speed
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create containers and groups for sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create player instance and add delta for the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw black screen
        screen.fill("black")

        # Iterate over groups and update their position and draw them
        for object in updatable:
            object.update(dt)
        
        for object in drawable:
            object.draw(screen)
        
        # Display the screen
        pygame.display.flip()

        # Limit framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
