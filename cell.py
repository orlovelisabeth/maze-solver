from visual import Point, Line

class Cell:

    def __init__(self, x1, x2, y1, y2, win=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
        self.x1 = x1
        self.x2 = x2 
        self.y1 = y1
        self.y2 = y2
        self.win = win

    def draw(self):
        if self.win is None:
            return
        top_left = Point(self.x1, self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_left = Point(self.x1, self.y2)
        bottom_right = Point(self.x2, self.y2)
        if self.left_wall:
            left = Line(top_left, bottom_left)
            self.win.draw_line(left)
        else: 
            left = Line(top_left, bottom_left)
            self.win.draw_line(left, "white")
        if self.right_wall:
            right = Line(top_right, bottom_right)
            self.win.draw_line(right)
        else:
            right = Line(top_right, bottom_right)
            self.win.draw_line(right, "white")
        if self.top_wall:
            top = Line(top_left, top_right)
            self.win.draw_line(top)
        else: 
            top = Line(top_left, top_right)
            self.win.draw_line(top, "white")
        if self.bottom_wall:
            bottom = Line(bottom_left, bottom_right)
            self.win.draw_line(bottom)
        else:
            bottom = Line(bottom_left, bottom_right)
            self.win.draw_line(bottom, "white")
    
    def draw_move(self, to_cell, undo=False):
        x = self.x1 + abs(self.x2 - self.x1) // 2
        y = self.y1 + abs(self.y2 - self.y1) // 2
        x2 = to_cell.x1 + abs(to_cell.x2 - to_cell.x1) // 2
        y2 = to_cell.y1 + abs(to_cell.y2 - to_cell.y1) // 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self.win.draw_line(Line(Point(x,y), Point(x2, y2)), fill_color)