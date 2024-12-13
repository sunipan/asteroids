import pygame

from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED


class Shot(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)