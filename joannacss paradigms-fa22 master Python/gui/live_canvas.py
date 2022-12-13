import tkinter as tk 

class CanvasExample:
	width = 500
	height = 500
	
	def __init__(self, root):
		self.root = root
		self.root.title("Canvas Example")
		
		# creates the canvas
		self.canvas = tk.Canvas(self.root, width=self.width,height=self.height)
		self.canvas.pack()

		# renders pet on the screen
		self.pets = [tk.PhotoImage(file="imgs/pea.png"), tk.PhotoImage(file="imgs/nash.png"), tk.PhotoImage(file="imgs/ravan.png")]
		self.curr_pet = 0
		self.pet = self.canvas.create_image(0, 0, image=self.pets[self.curr_pet], anchor=tk.NW)

		# register events
		self.root.bind("<Up>", self.move)
		self.root.bind("<Down>", self.move)
		self.root.bind("<Left>", self.move)
		self.root.bind("<Right>", self.move)
		self.root.bind("<Button-2>", self.change)
		self.root.bind("<B1-Motion>", self.drag)

	def drag(self, event):
		widget = event.widget
		xc = widget.canvasx(event.x)
		yc = widget.canvasy(event.y)
		previous = self.canvas.coords(self.pet)
		self.canvas.move(self.pet, xc - previous[0], yc - previous[1])

	def change(self, event):
		self.curr_pet = (self.curr_pet  + 1) % len(self.pets)
		self.canvas.itemconfig(self.pet, image=self.pets[self.curr_pet])


	def move(self, event):
		d = event.keysym
		if d == "Right":
			self.canvas.move(self.pet, 5, 0)
		if d == "Left":
			self.canvas.move(self.pet, -5, 0)
		if d == "Up":
			self.canvas.move(self.pet, 0, -5)
		if d == "Down":
			self.canvas.move(self.pet, 0, 5)
			
	
if __name__ == '__main__':
	# creates main window
	root = tk.Tk()
	# instantiates our UI class
	app = CanvasExample(root)
	# enters the main loop
	root.mainloop()
