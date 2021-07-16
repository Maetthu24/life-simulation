from tkinter import *
from entity import Entity
from grid import Grid
import random

# Constants
WINDOW_HEIGHT = 1200
WINDOW_WIDTH = 1600


def run_draw_loop(window, canvas, grid, counter):
	grid.move_entities()

	window.after(500, run_draw_loop, window, canvas, grid, counter)


if __name__ == '__main__':
	
	# Create window	& canvas
	window = Tk()
	window.title("Life Simulation by Luki, Dave & Mätthe")
	window.geometry(str(WINDOW_HEIGHT) + 'x' + str(WINDOW_WIDTH))
	
	canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bd=0, highlightthickness=0, relief='ridge')
	
	# Create grid
	grid = Grid(20, 20, 40, canvas)
	spawned = grid.spawn_random_entity()
	while not spawned:
		spawned = grid.spawn_random_entity()
	
	canvas.pack(fill=BOTH, expand=0)
	
	counter = 0
	run_draw_loop(window, canvas, grid, counter)

	window.mainloop()
