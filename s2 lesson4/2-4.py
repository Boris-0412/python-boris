from pycat.base.color import Color
from pycat.core import Window
from pycat.sprite import Sprite
import random

window = Window()

class Cell(Sprite):

    def on_create(self):
        self.width = 20
        self.height = 20
       

    def make_label(self, value, min, max):
        label = window.create_label()
        label.x = self.x
        label.y = self.y
        label.text = str(value)
        label.color = Color.ORANGE
        label.font_size = 10
        scale = (value - min)/(max - min)
        self.color = (255,255*(1-scale),255*(1-scale))

        


my_list = []

for i in range(10):
    my_list.append([random.randint(0,100) for j in range(20)])

min_val = max_val = my_list[1][0]
for i in range(3):
    for j in range(4):
        v = my_list[i][j]
        if min_val > v:
            min_val = v
        if max_val < v:
            max_val = v

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
       cell = window.create_sprite(Cell)
    #    cell = str(my_list[i][j])
       cell.x = 500 + (cell.width + 10)*j
       cell.y = 400 - (cell.height + 10)*i
       cell.make_label(my_list[i][j], min_val, max_val)
       

    
       


window.run()