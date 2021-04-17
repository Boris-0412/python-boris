from pycat.core import Window, Sprite
import random
window = Window()

class Turtle(Sprite):

    def draw_forward(self, distance):
        x = self.x
        y = self.y
        self.move_forward(distance)
        window.create_line(x, y, self.x, self.y)

    def draw_rect(self, width, height):
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)
        self.rotation += 90
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)

class Building:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, t:Turtle):
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.w, self.h)


t = window.create_sprite(Turtle)
b = Building(0, 0, 75, 200)
for i in range(10):
    b.x += 100
    b.h = random.randint(200,500)
    b.draw(t)



window.run()