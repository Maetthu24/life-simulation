import random

class Entity:

	def __init__(self, pos_x, pos_y, color = None):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.is_alive = True

		if color:
			self.color = color
		else:
			# Create random color
			r = lambda: random.randint(0,255)
			c = '#%02X%02X%02X' % (r(),r(),r())
			self.color = c


	def move(self, dir_x, dir_y):
		self.pos_x = dir_x
		self.pos_y = dir_y
