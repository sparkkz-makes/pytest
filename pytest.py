from tkinter import *

width, height = 600, 500
tk = Tk()
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Ball:
    def __init__(self, x, y, vx, vy, size, color):
        self.ball = canvas.create_oval(x, y, x+size, y+size, fill=color)
        self.vx = vx
        self.vy = vy
        self.move()

    def move(self):
        canvas.move(self.ball, self.vx, self.vy)
        pos = canvas.coords(self.ball)
        if pos[2] >= width or pos[0] <= 0:
            self.vx *= -1
        if pos[3] >= height or pos[1] <= 0:
            self.vy *= -1
        tk.after(10, self.move)


ball = Ball(10,10,2,1,10,'blue')
tk.mainloop()