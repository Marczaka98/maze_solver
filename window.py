from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill = fill_color,
            width = 5
        )
    
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x1,y2))
            self._win.draw_line(line,"white")
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line,"white")
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line,"white")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2),Point(x2,y2))
            self._win.draw_line(line,"white")

    def draw_move(self, to_cell, undo=False):
        starting_point = Point((self._x1 + self._x2)//2,(self._y1 + self._y2)//2)
        ending_point = Point((to_cell._x1 + to_cell._x2)//2,(to_cell._y1 + to_cell._y2)//2)
        if undo:
            self._win.draw_line(Line(starting_point,ending_point),"red")
        else:
            self._win.draw_line(Line(starting_point,ending_point),"green")
        