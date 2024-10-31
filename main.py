import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize game and add constants for screen size and clock speed
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create groups for sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Create containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create player instance, asteroid_field instance, and add delta
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw black screen
        screen.fill("black")

        # Update objects positions
        for object in updatable:
            object.update(dt)
        
        # Check if the asteroid has collided with the player
        for asteroid in asteroids:
            game_over = asteroid.collided(player)
            if game_over:
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collided(shot):
                    asteroid.split()
                    shot.kill()
        
        # Draw all objects on screen
        for object in drawable:
            object.draw(screen)
        
        # Display the screen
        pygame.display.flip()

        # Limit framerate
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
