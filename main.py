import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player
from shot import Shot 


def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  Shot.containers = (shots, updatables, drawables)

  AsteroidField().spawn(ASTEROID_MIN_RADIUS, pygame.Vector2(0, 0), pygame.Vector2(0, 0))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill((0, 0, 0))
    for updatable in updatables:
      updatable.update(dt)
    
    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        print("Game Over!")
        exit()
      for shot in shots:
        if asteroid.is_colliding(shot):
          asteroid.split()

    for drawable in drawables:
      drawable.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()