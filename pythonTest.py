from tkinter import *

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

window = Tk()
window.title("DLM")
window.geometry(str(WINDOW_HEIGHT) + 'x' + str(WINDOW_WIDTH))

canvas = Canvas(window)

tilesX = WINDOW_WIDTH/10
tilesY = WINDOW_HEIGHT/10

for x in range(tilesX-1):
    for y in range(tilesY-1):
        if (x+y) % 2 == 0:
            canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#333", fill="#333")
        else:
            canvas.create_rectangle(x*10, y*10, x*10+10, y*10+10, outline="#ddd", fill="#ddd")

canvas.pack(fill=BOTH, expand=1)

window.mainloop()

