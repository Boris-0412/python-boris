from pycat.base.color import Color
from pycat.core import Window, Sprite
from random import choice
from typing import List
HEIGHT = 900
WIDTH = 500
window = Window(width = WIDTH, height = HEIGHT)

class Choices(Sprite):
    current_color = None

    def on_create(self):
        self.x = 75
        self.y = 100
        self.scale = 50

    def on_left_click(self):
        Choices.current_color = self.color
        

color_list = [Color.RED,
Color.BLUE, 
Color.YELLOW, 
Color.ORANGE]

for i in range(4):
    c = window.create_sprite(Choices)
    c.x += i*(c.width + 50)
    c.color = color_list[i]


class CheckButton(Sprite):

    def on_create(self):
        self.x = 450
        self.y = 100
        self.scale = 25    

    def on_left_click(self):
        for i in range(4):
            if guess_list[i].color == code_list[i].color:
                print("same", i)
            
            else:
                print("not same", i)
        print("---------------")

class Guess(Sprite):

    def on_create(self):
        self.x = 75
        self.y = 200
        self.scale = 50

    def on_left_click(self):
        if Choices.current_color is not None:
            self.color = Choices.current_color

guess_list: List[Guess] = []
for i in range(4):
    c = window.create_sprite(Guess)
    c.x += i*(c.width + 50)
    guess_list.append(c)

class ColorCode(Sprite):

    def on_create(self):
        self.scale = 50
        self.x = 75
        self.y = window.height - (self.height/2 + 50)
        
code_list: List[ColorCode] = []
for i in range(4):
    c = window.create_sprite(ColorCode)
    c.x += i*(c.width + 50)
    c.color = choice(color_list)
    code_list.append(c)
    
window.create_sprite(CheckButton)

window.run()