from window import *

win = Window(800,600)

point1, point2 = Point(10,10), Point(20,20)
point3, point4 = Point(20,20), Point(50,50)
line = Line(point1,point2)
line2 = Line(point3,point4)

win.draw_line(line,"black")
win.draw_line(line2,"red")

win.wait_for_close()
