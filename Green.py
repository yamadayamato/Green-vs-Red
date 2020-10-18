import pygame
import colors
from advanced_math import *
from config import *
from Bullet import Bullet


class Green:
	size = 20
	cooldown = 1000

	def __init__(self, position):
		self.position = position
		self.inital_ticks = pygame.time.get_ticks()
		self.final_ticks = self.inital_ticks

	def draw(self, surface):
		"""
		Draws the green object on a surface
		:param surface: Surface
		:return: None
		"""
		pygame.draw.circle(surface, colors.earth_green, self.position.to_tuple(), Green.size)

	def bullet_events(self):
		"""
		Used to trigger bullet events for a green object
		:return: Bullet or None
		"""
		self.final_ticks = pygame.time.get_ticks()
		if(self.final_ticks - self.inital_ticks >= Green.cooldown):
			self.inital_ticks = self.final_ticks
			return Bullet(Vector2(self.position.x, self.position.y))
		else:
			return None
