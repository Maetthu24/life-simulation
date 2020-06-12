class Grid:
	"""docstring for Grid"""
	def __init__(self, tilesX, tilesY, tilesize, canvas):
		self.tilesX = tilesX
		self.tilesY = tilesY
		self.tilesize = tilesize
		self.canvas = canvas

		


		for x in range(self.tilesX):
		    for y in range(self.tilesY):
		        if (x+y) % 2 != 0:
		            self.canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#333", fill="#333")
		        else:
		            self.anvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#ddd", fill="#ddd")