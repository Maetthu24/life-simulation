import random

class Entity:

	def __init__(self, posX, posY):
		self.posX = posX
		self.posY = posY
		self.isAlive = True

		r = lambda: random.randint(0,255)
		c = '#%02X%02X%02X' % (r(),r(),r())
		print(c)
		self.color = c

	def move(self, dirX, dirY):
		self.posX = self.posX + dirX
		self.posY = self.posY + dirY
