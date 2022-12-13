import tkinter as tk
from tkinter import Canvas, Tk

class MoveRobotCanvas:
    width = 400
    height = 300
    def __init__(self, root):
        self.root = root
        self.root.title("Move Robot q3")
        self.m = 0

        # create canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        for i in range(int(self.width/10)):
            self.canvas.create_line(10*i, 0, 10*i, 300, fill="red")
        for j in range(int(self.height/10)):
            self.canvas.create_line(0, 10*j, 400, 10*j, fill="red")


        # renders robot on screen
        self.img = tk.PhotoImage(file="robot-24x24.png")
        self.robot = self.canvas.create_image(int(self.width/2), int(self.height/2), image = self.img)
        print(tuple(self.canvas.coords(self.robot)))
        self.root.bind("<Button-1>", self.move_robot)

    def move_robot(self, event):
        
        self.center = self.canvas.coords(self.robot)
        face = (self.m) % 4
        if face == 0:
            # move north
            self.upper = self.center[1] - 12 - 10*(self.m+1)
            self.lower = self.center[1] + 12 - 10*(self.m+1)
            self.left = self.center[0] - 12
            self.right = self.center[0] + 12
            self.check_bounds()
            self.canvas.move(self.robot, 0, -10*(self.m + 1))
        elif face == 1:
            # move east
            self.upper = self.center[1] - 12
            self.lower = self.center[1] + 12
            self.left = self.center[0] - 12 + 10*(self.m + 1)
            self.right = self.center[0] + 12 + 10*(self.m + 1)
            self.check_bounds()
            self.canvas.move(self.robot, 10*(self.m + 1), 0)
        elif face == 2:
            # move south
            self.upper = self.center[1] - 12 + 10*(self.m+1)
            self.lower = self.center[1] + 12 + 10*(self.m+1)
            self.left = self.center[0] - 12
            self.right = self.center[0] + 12
            self.check_bounds()
            self.canvas.move(self.robot, 0, 10*(self.m + 1))
        else:
            # move west
            self.upper = self.center[1] - 12
            self.lower = self.center[1] + 12
            self.left = self.center[0] - 12 - 10*(self.m + 1)
            self.right = self.center[0] + 12 - 10*(self.m + 1)
            self.check_bounds()
            self.canvas.move(self.robot, -10*(self.m + 1), 0)
        self.m += 1
        print(tuple(self.canvas.coords(self.robot)))
    def check_bounds(self):
        # check if in bounds
        if self.upper < 0 or self.lower > self.height or self.left < 0 or self.right > self.width:
            self.reset()
    def reset(self):
        self.m = -1
        canvas_center = [self.width/2, self.height/2]
        self.canvas.move(self.robot, canvas_center[0] -  self.center[0], canvas_center[1] - self.center[1])



if __name__ == '__main__':
    root = Tk()
    robot = MoveRobotCanvas(root)
    
    root.mainloop()