from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title('Maze Solver')
        self.root.protocol("WM_DELETE_WINDOW", self.close) 
        self.canvas = Canvas(self.root, height=height, width=width, bg="white")
        self.canvas.pack()
        self.is_running = False


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start.x, 
            self.start.y, 
            self.end.x, 
            self.end.y, 
            fill=fill_color, 
            width=2
            )