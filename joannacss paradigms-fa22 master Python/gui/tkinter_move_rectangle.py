from tkinter import Canvas, Tk
import time


def move_rectangle(event):
	# move method (object you want to move, and the direction!)
	# .move (object, xAmount, yAmount )
	c.move(rectangle, 1, 1)
		

root = Tk()
c = Canvas(root, width=400, height=200)
c.pack()
rectangle = c.create_rectangle(50, 25, 100, 75, fill="blue")
root.bind("<Button-1>", move_rectangle)
root.mainloop()

