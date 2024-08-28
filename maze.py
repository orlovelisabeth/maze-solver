import time
import random
from visual import Point, Line
from cell import Cell



class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed:
            self.seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):

        if self.num_rows == 0 or self.num_cols == 0:
            raise Exception(f"Invalid matrix size: rows and columns must be greater than 0")
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                x1 = self.x1 + self.cell_size_x * i 
                x2 = x1 + self.cell_size_x
                y1 = self.y1 + self.cell_size_y * j 
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, x2, y1, y2, self.win)
                col.append(cell)
            self._cells.append(col)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True

        while True:

            to_visit = []

            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))


            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            index = random.randrange(len(to_visit))
            (v,w) = to_visit[index]

            if v == i-1:
                self._cells[i][j].left_wall = False
                self._cells[v][w].right_wall = False
            if v == i+1:
                self._cells[i][j].right_wall = False
                self._cells[v][w].left_wall = False
            if w == j-1:
                self._cells[i][j].top_wall = False
                self._cells[v][w].bottom_wall = False
            if w == j+1:
                self._cells[i][j].bottom_wall = False
                self._cells[v][w].top_wall = False

                
            self._break_walls_r(v, w)


    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):

        self._animate()

        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        if i > 0 and \
            not self._cells[i-1][j].visited and \
            not self._cells[i][j].left_wall:
                
                self._cells[i][j].draw_move(self._cells[i-1][j])

                if self._solve_r(i-1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j], True)
            
        if i < self.num_cols - 1 and \
            not self._cells[i+1][j].visited and \
            not self._cells[i][j].right_wall:
                
                self._cells[i][j].draw_move(self._cells[i+1][j])

                if self._solve_r(i+1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j], True)
            
        if j > 0 and \
            not self._cells[i][j-1].visited and \
            not self._cells[i][j].top_wall:
                
                self._cells[i][j].draw_move(self._cells[i][j-1])

                if self._solve_r(i, j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1], True)

        if j < self.num_rows - 1 and \
            not self._cells[i][j+1].visited and \
                not self._cells[i][j].bottom_wall:

                self._cells[i][j].draw_move(self._cells[i][j+1])

                if self._solve_r(i, j+1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False