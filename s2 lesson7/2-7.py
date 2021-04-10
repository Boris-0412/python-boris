from pycat.core import Window, Point, Color
from math import sqrt

window = Window()

A = Point(600,300)
B = Point(800,300)

c = A.x - B.x
a = c/2
b = sqrt(c**2 - a**2)

C = Point((A.x + B.x)/2,A.y + b)

window.create_line(A.x, A.y, B.x, B.y, width = 1000, color = Color.CYAN)
window.create_line(B.x, B.y, C.x, C.y, width = 1000, color = Color.GREEN)
window.create_line(C.x, C.y, A.x, A.y, width = 1000, color = Color.ORANGE)


window.run()