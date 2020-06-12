class Grid:
	def __init__(self, tilesX, tilesY, tilesize, canvas):
		self.tilesX = tilesX
		self.tilesY = tilesY
		self.tilesize = tilesize
		self.canvas = canvas

		for x in range(self.tilesX):
			for y in range(self.tilesY):
				if (x+y) % 2 != 0:
					self.canvas.create_rectangle(x*tilesize, y*tilesize, x*tilesize+tilesize, y*tilesize+tilesize, outline="", fill="#333")
				else:
					self.canvas.create_rectangle(x*tilesize, y*tilesize, x*tilesize+tilesize, y*tilesize+tilesize, outline ="", fill="#ddd")

	def drawEntity(self, entity):
		tilesize = self.tilesize
		print(tilesize)
		self.canvas.create_oval(entity.posX*tilesize, entity.posY*tilesize, entity.posX*tilesize+tilesize, entity.posY*tilesize+tilesize, fill=entity.color)
