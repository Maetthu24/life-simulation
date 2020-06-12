from tkinter import *
from entity import Entity
from grid import Grid
import random

if __name__ == '__main__':

	WINDOW_HEIGHT = 500
	WINDOW_WIDTH = 500
	
	window = Tk()
	window.title("Life Simulation by Luki, Dave & Mätthe")
	window.geometry(str(WINDOW_HEIGHT) + 'x' + str(WINDOW_WIDTH))
	
	canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bd=0, highlightthickness=0, relief='ridge')
	
	g = Grid(10,10,40,canvas)
	
	canvas.pack(fill=BOTH, expand=0)
	e1 = Entity(random.randint(0,10-1), random.randint(0,10-1))
	#    print(e1.posX)
	#    print(e1.posY)
	
	g.drawEntity(e1)
	
	window.mainloop()
