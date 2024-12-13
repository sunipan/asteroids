import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player 


def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = drawable

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  updatable.add(player)
  drawable.add(player)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill((0, 0, 0))
    for update in updatable:
      update.update(dt)
    for draw in drawable:
      draw.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()