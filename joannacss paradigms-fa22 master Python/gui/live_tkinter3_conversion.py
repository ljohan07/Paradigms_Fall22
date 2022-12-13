from tkinter import *
from tkinter import messagebox


class InfoWindow:
	def __init__(self, root):
		self.root = root
		self.root.title("Formula information")
		self.label = Label(self.root, text="The formula is to multiply by 0.3048")
		self.label.pack()



class ConversionWindow:
	
	def convert(self, *args):
		try:
			value = float(self.feet.get())
			if value < 0: raise ValueError()
			self.meters.set( round(0.3048 * value, 2) )
		except ValueError:
			messagebox.showinfo(title="Error!", message= "Please provide a valid number")

	def viewFormula(self, *args):
		self.infoWindow = InfoWindow(Toplevel(self.root))


	def __init__(self, root):
		self.root = root
		
		self.mainFrame = Frame(root, padx=10, pady=10)
		self.mainFrame.grid(row=0, column=0)
		
		self.feet = StringVar()
		self.feetEntry = Entry(self.mainFrame, width=7, textvariable=self.feet)
		self.feetEntry.grid(row=0, column=1)

		self.meters = StringVar()
		Label(self.mainFrame, textvariable=self.meters).grid(row=1, column=1)

		Button(self.mainFrame, text="View Formula", command=self.viewFormula).grid(row=2, column=1)
		Button(self.mainFrame, text="Calculate", command=self.convert).grid(row=2, column=2)
		
		Label(self.mainFrame, text="feet").grid(row=0, column=2)
		Label(self.mainFrame, text="is equivalent to").grid(row=1, column=0)
		Label(self.mainFrame, text="meters").grid(row=1, column=2)
		
		for c in self.mainFrame.winfo_children():
			c.grid_configure(padx=5,pady=5)

		self.feetEntry.focus()
		self.feetEntry.bind("<Return>", self.convert)

if __name__ == '__main__':
	root = Tk()
	root.title("Feet to Meters")
	window = ConversionWindow(root)
	root.mainloop()
