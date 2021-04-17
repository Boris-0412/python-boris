from pycat.core import Window as W, Sprite
import random
window = W()

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
        self.window = [
            [
            Window(x, y, 10, 10)
            for y in range(self.y + 10,self.y+ self.h - 15,20)
            ]
            for x in range(self.x + self.w//2 + 10,self.x, -20)
        ]

    def draw(self, t:Turtle):
        for col in self.window:
            for w in col:
                w.draw(t)
        
        t.rotation = 0
        t.x = self.x
        t.y = self.y
        t.draw_rect(self.w, self.h)

class Window:

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
x = 100
for i in range(10):
    b = Building(x, 0, random.randint(50,100), random.randint(200,500))
    x += b.w + 30
    b.draw(t)




window.run()