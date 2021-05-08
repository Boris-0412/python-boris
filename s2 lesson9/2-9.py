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
        self.guess = 0 
        self.red_pegs = 0
        self.white_pegs = 0

    def count_pegs(self):
        maybe_white_code = []
        maybe_white_guess = []
        for i in range(4):
            if guess_list[i].color == code_list[i].color:
                self.red_pegs += 1
            else:
                maybe_white_code.append(code_list[i].color)
                maybe_white_guess.append(guess_list[i].color)

        for c in maybe_white_guess:
            if c in maybe_white_code:
                self.white_pegs += 1
                maybe_white_code.remove(c)

    def on_left_click(self):        
        self.count_pegs()
        draw_pegs(self.guess, self.red_pegs, self.white_pegs)
        if self.red_pegs == 4:
            print("You win!")
        else:            
            self.guess += 1
            make_new_guess(self.guess)
            self.red_pegs = 0
            self.white_pegs = 0

def make_new_guess(guess):
    guess_list.clear()
    if guess < 8:
        for i in range(4):
            c = window.create_sprite(Guess)
            c.x += i*(c.width + 50)
            c.y += guess*(c.height + 25)
            guess_list.append(c)
    else:
        print("You lose!")
        window.close()
    
def draw_pegs(guess, red_pegs, white_pegs):
    for i in range(red_pegs + white_pegs):
        d = window.create_sprite()
        if i < red_pegs:
            d.color = Color.RED
        else:
            d.color = Color.WHITE
        d.scale = 10
        d.x = check.x + i*(d.width + 5)
        d.y = 200
        d.y += guess*(c.height + 25)



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
        self.is_visible = False
        self.scale = 50
        self.x = 75
        self.y = window.height - (self.height/2 + 50)
        
code_list: List[ColorCode] = []
for i in range(4):
    c = window.create_sprite(ColorCode)
    c.x += i*(c.width + 50)
    c.color = choice(color_list)
    code_list.append(c)
    
check = window.create_sprite(CheckButton)

window.run()