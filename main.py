from visual import Window, Point, Line
from maze import Maze
from cell import Cell

def main():
    win = Window(800, 600)

    p1 = Point(100, 100)
    p2 = Point(300, 300)
    p3 = Point(400, 100)
    p4 = Point(500, 300)

    test = Cell(p1.x, p2.x, p1.y, p2.y, win)
    test2 = Cell(p3.x, p4.x, p3.y, p4.y, win)

    maze = Maze(50, 50, 10, 14, 50, 50, win)

    maze._break_walls_r(0,0)
    maze._reset_cells_visited()

    maze.solve()

    win.wait_for_close()





main()