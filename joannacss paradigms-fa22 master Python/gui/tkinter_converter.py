from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class InfoWindow:
    # initializes the UI elements
    def __init__(self, root):
        self.root = root       
        self.root.title("Formula information")
        self.label = Label(root, text="To convert ft to m, you need to multiply your length value by 0.3048.\n The formula is m = ft × 0.3048")
        self.label.pack()



class ConversionWindow:
    
    def convert(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set( round(0.3048 * value, 2) )
        except ValueError as e:
            messagebox.showerror(title="Error!", message=e)

    def viewInfo(self):
        self.infoWindow = Toplevel(self.root)
        InfoWindow(self.infoWindow)


    def __init__(self, root):
        self.root = root
        
        self.mainframe = Frame(root, padx=3,pady=12)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.root.columnconfigure(0, weight=1)  # fill in extra space
        self.root.rowconfigure(0, weight=1)     # fill in extra space

        self.feet = StringVar()
        self.feet_entry = Entry(self.mainframe, width=7, textvariable=self.feet)
        self.feet_entry.grid(column=2, row=1, sticky=(W, E))

        self.meters = StringVar()
        Label(self.mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))

        Button(self.mainframe, text="Calculate", command=self.convert).grid(column=3, row=3, sticky=W)
        Button(self.mainframe, text="View Formula", command=self.viewInfo).grid(column=2, row=3, sticky=W)

        Label(self.mainframe, text="feet").grid(column=3, row=1, sticky=W)
        Label(self.mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        Label(self.mainframe, text="meters").grid(column=3, row=2, sticky=W)

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.feet_entry.focus()
        self.feet_entry.bind("<Return>", self.convert)

if __name__ == '__main__':
    root = Tk()
    root.title("Feet to Meters")
    window = ConversionWindow(root)
    root.mainloop()
