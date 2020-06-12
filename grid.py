from entity import Entity
import random

class Grid:

	def __init__(self, tiles_x, tiles_y, tile_size, canvas):
		self.tiles_x = tiles_x
		self.tiles_y = tiles_y
		self.tile_size = tile_size
		self.canvas = canvas

		self.grid_representation = [[0 for x in range(tiles_x-1)] for y in range(tiles_y-1)]

		self.entities = []

		# Create and draw chess board grid
		for x in range(self.tiles_x-1):
			for y in range(self.tiles_y-1):
				if (x+y) % 2 != 0:
					col = '#333'
				else:
					col = '#ddd'

				self.canvas.create_rectangle(
					x * tile_size,
					y * tile_size,
					(x+1) * tile_size,
					(y+1) * tile_size,
					outline = '',
					fill = col)


	def spawn_random_entity(self):
		e = Entity(random.randint(0, self.tiles_x-2), random.randint(0, self.tiles_y-2))
		ts = self.tile_size

		# Check if grid position is empty and object can spawn
		if self.is_empty(e.pos_x, e.pos_y):
			# Draw entity as circle
			e.object_id = self.canvas.create_oval(
				e.pos_x * ts,
				e.pos_y * ts,
				(e.pos_x+1) * ts,
				(e.pos_y+1) * ts,
				fill = e.color)

			self.entities.append(e)
			self.grid_representation[e.pos_x][e.pos_y] = 1
			return True
		else:
			return False

	def spawn_entity(self, x, y, color = None):
		e = Entity(x, y, color = color)
		ts = self.tile_size

		if self.is_empty(x, y):
			# Draw entity as circle
			e.object_id = self.canvas.create_oval(
				e.pos_x * ts,
				e.pos_y * ts,
				(e.pos_x+1) * ts,
				(e.pos_y+1) * ts,
				fill = e.color)

			self.entities.append(e)
			self.grid_representation[e.pos_x][e.pos_y] = 1
			return True
		else:
			return False


	def move_entities(self):
		for e in self.entities:
			# For each entity, try to find empty neighbor cells in the grid
			n = self.find_empty_neighbours(e.pos_x, e.pos_y)

			if len(n) > 0:
				# If there are empty neighbor cells, move to one of them with probability 0.7
				# and leave offspring at old cell with probability 0.3
				dice = random.uniform(0, 1)
				if dice > 0.3:
					new_pos = random.choice(n)
					old_pos = (e.pos_x, e.pos_y)
					self.move_entity(e, new_pos[0], new_pos[1])
					dice = random.uniform(0, 1)
					if dice > 0.7:
						self.spawn_entity(old_pos[0], old_pos[1], color = e.color)

			# Let entity die with probability 0.1
			dice = random.uniform(0, 1)
			if dice > 0.9:
				self.canvas.delete(e.object_id)
				self.entities.remove(e)
				self.grid_representation[e.pos_x][e.pos_y] = 0

	
	def move_entity(self, e, x, y):
		if self.grid_representation[x][y] != 0:
			return

		ts = self.tile_size

		self.grid_representation[e.pos_x][e.pos_y] = 0
		e.move(x, y)
		self.canvas.delete(e.object_id)
		e.object_id = self.canvas.create_oval(
			e.pos_x * ts,
			e.pos_y * ts,
			(e.pos_x+1) * ts,
			(e.pos_y+1) * ts,
			fill = e.color)

		self.grid_representation[e.pos_x][e.pos_y] = 1


	def is_empty(self, x, y):
		return self.grid_representation[x][y] == 0


	def find_empty_neighbours(self, x, y):
		neighbours = []
		
		if x > 0 and self.grid_representation[x-1][y] == 0:
			neighbours.append((x-1, y))
		if y > 0 and self.grid_representation[x][y-1] == 0:
			neighbours.append((x, y-1))
		if x < self.tiles_x - 2 and self.grid_representation[x+1][y] == 0:
			neighbours.append((x+1, y))
		if y < self.tiles_y - 2 and self.grid_representation[x][y+1] == 0:
			neighbours.append((x, y+1))

		return neighbours

