# TODO: import statements
import tkinter
from tkinter import messagebox

def greet():
	messagebox.showinfo(title="Greetings", message="Hi user!")

# TODO: create root (main) window
top = tkinter.Tk()


# TODO: add some widgets (UI elements)
label = tkinter.Label(top, text="An example label")
label.pack()


button = tkinter.Button(top, text="Greet!", command=greet)
button.pack()

button2 = tkinter.Button(top, text="Quit", command=top.quit)
button2.pack()


# TODO: trigger main loop

top.mainloop()

