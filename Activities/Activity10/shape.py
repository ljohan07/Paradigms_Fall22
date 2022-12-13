from tkinter import Canvas, Tk
from turtle import bgcolor

root = Tk()

w = Canvas(root, width=400, height=300)
w.pack()

# x0, y0, x1, y1
center_x = 400/2
center_y = 300/2
x0 = center_x - 15/2
x1 = center_x + 15/2
y0 = center_y - 15/2
y1 = center_y + 15/2
w.create_rectangle(x0, y0, x1, y1, fill="blue")

root.mainloop()