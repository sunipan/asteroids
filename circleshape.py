import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
      # we will be using this later
      super().__init__()
      if hasattr(self, "containers"):
          for container in self.containers:
              container.add(self)

      self.position = pygame.Vector2(x, y)
      self.velocity = pygame.Vector2(0, 0)
      self.radius = radius

    def draw(self, screen):
      # sub-classes must override
      pass

    def update(self, dt):
      # sub-classes must override
      pass
    
    def is_colliding(self, other):
      return self.position.distance_to(other.position) <= (self.radius + other.radius)