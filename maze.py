from window import *
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
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
            random.seed(seed)
        else:
            random.seed()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(0,self.num_cols):
            self._cells.append([])
            for j in range(0,self.num_rows):
                self._cells[i].append(Cell(self.win))

        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell_x1 = self.x1 + i * self.cell_size_x
        cell_y1 = self.y1 + j * self.cell_size_y
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1,self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #left
            if i > 0 and self._cells[i-1][j].visited == False: 
                to_visit.append([i-1,j,'left'])
            #right
            if i < self.num_cols - 1 and self._cells[i+1][j].visited == False: 
                to_visit.append([i+1,j,'right'])
            #up
            if j > 0 and self._cells[i][j-1].visited == False: 
                to_visit.append([i,j-1,'up'])
            #down
            if j < self.num_rows - 1 and self._cells[i][j+1].visited == False: 
                to_visit.append([i,j+1,'down'])
            if not to_visit:
                self._draw_cell(i,j)
                return
            rand_direction = random.randrange(0,len(to_visit))
            c_i, c_j, direction = to_visit[rand_direction][0],to_visit[rand_direction][1],to_visit[rand_direction][2]
            if direction == 'right':
                self._cells[i][j].has_right_wall = False
                self._cells[c_i][c_j].has_left_wall = False
            if direction == 'down':
                self._cells[i][j].has_bottom_wall = False
                self._cells[c_i][c_j].has_top_wall = False
            if direction == 'left':
                self._cells[i][j].has_left_wall = False
                self._cells[c_i][c_j].has_right_wall = False
            if direction == 'up':
                self._cells[i][j].has_top_wall = False
                self._cells[c_i][c_j].has_bottom_wall = False
            self._break_walls_r(c_i,c_j)

    def _reset_cells_visited(self):
        for i in range(0,self.num_cols):
            for j in range(0,self.num_rows):
                self._cells[i][j].visited = False
                
    def solve(self):
        return self._solve_r()
    
    def _solve_r(self,i=0,j=0):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        #left
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)
        #right
        if i < self.num_cols - 1 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)
        #up
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)
        #down
        if j < self.num_rows - 1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)
        return False
        