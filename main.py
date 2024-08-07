from window import *

win = Window(800,600)

# point1, point2 = Point(10,10), Point(20,20)
# point3, point4 = Point(20,20), Point(50,50)
# line = Line(point1,point2)
# line2 = Line(point3,point4)

# win.draw_line(line,"black")
# win.draw_line(line2,"red")

# cell1 = Cell(50,50,100,100,win,True,True,True,False)
# cell2 = Cell(100,50,150,100,win)
# cell3 = Cell(150,50,200,100,win)
# cell4 = Cell(200,50,250,100,win)
# cell5 = Cell(250,50,300,100,win)
cell1 = Cell(win)
cell2 = Cell(win)
cell3 = Cell(win)

cell1.has_right_wall = False
cell1.draw(50,50,100,100)

cell2.has_left_wall = False
cell2.has_right_wall = False
cell2.draw(100,50,150,100)

cell3.has_left_wall = False
cell3.draw(150,50,200,100)

cell1.draw_move(cell3,True)

win.wait_for_close()
