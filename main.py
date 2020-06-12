from tkinter import *
from entity import Entity
import random

if __name__ == '__main__':

	WINDOW_HEIGHT = 500
	WINDOW_WIDTH = 500

	window = Tk()
	window.title("Life Simulation by Luki, Dave & Mätthe")
	window.geometry(str(WINDOW_HEIGHT) + 'x' + str(WINDOW_WIDTH))

	canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bd=0, highlightthickness=0, relief='ridge')

	tilesX = int(WINDOW_WIDTH/10)
	tilesY = int(WINDOW_HEIGHT/10)

	for x in range(tilesX):
	    for y in range(tilesY):
	        if (x+y) % 2 != 0:
	            canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#333", fill="#333")
	        else:
	            canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#ddd", fill="#ddd")
	            
	canvas.config()

	canvas.pack(fill=BOTH, expand=0)

	e1 = Entity(random.randint(0,tilesX-1), random.randint(0,tilesY-1))
	print(e1.posX)
	print(e1.posY)
	canvas.create_oval()

	window.mainloop()
