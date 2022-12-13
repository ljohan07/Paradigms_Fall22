from tkinter import Canvas, Tk

root = Tk()

w = Canvas(root, width=400, height=200)
w.pack()

# x0, y0, x1, y1
w.create_line(20, 20, 50, 50, fill="magenta") 

# x0, y0, x1, y1
w.create_rectangle(20, 20, 50, 50, outline="blue")

root.mainloop()

