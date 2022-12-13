from tkinter import Canvas, Tk

root = Tk()

w = Canvas(root, width=400, height=300)
w.pack()

# x0, y0, x1, y1
w.create_line(0, 0, 400, 200) 
# x0, y0, x1, y1
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# x0, y0, x1, y1
w.create_rectangle(190, 140, 210, 160, fill="blue")

root.mainloop()