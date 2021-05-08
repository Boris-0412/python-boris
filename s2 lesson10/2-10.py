from enum import Enum
from pycat.base.color import Color
from pycat.core import Window, Scheduler
from pycat.geometry import point
from pycat.sprite import Sprite
from random import randint, choice
w = Window(enforce_window_limits=False)

sports =['basketball', 'soccer', 'baseball', 'volleyball']
cars = ['Toyota', 'Volvo', 'Benz', 'Honda']
animals = ['dog', 'cat', 'panda', 'hamster']
words = sports + cars + animals

class State(Enum):
    SPORTS = 0
    CARS = 1
    ANIMALS = 2

states = [State.SPORTS, State.CARS, State.ANIMALS]
current_state = choice(states)

def change_state():
    global current_state
    current_state = choice(states)
    print(current_state)

Scheduler.update(change_state, delay=3)

class Word(Sprite):
    point = 0

    def on_create(self):
        self.label = w.create_label()
        self.label.font_size = 40
        self.label.color = Color.WHITE
        self.color = Color.random_rgb()
        self.image = 'block.png'

    def background(self, text, x, y):
        self.label.text = text
        self.height = self.label.content_height
        self.width = self.label.content_width
        self.x = x
        self.y = y
        self.label.x = x - self.width/2
        self.label.y = y + self.height/2

    def on_update(self, dt):
        fall_speed = 5
        self.y -= fall_speed
        self.label.y -= fall_speed
        if self.y < 0:
            self.delete()
            self.label.delete()

    def on_left_click(self):
        if current_state == State.ANIMALS and self.label.text in animals:
            self.delete()
            self.label.delete()
            Word.point += 1
            print(self.point)
        elif current_state == State.SPORTS and self.label.text in sports:
            self.delete()
            self.label.delete()
            Word.point += 1
            print(self.point)
        elif current_state == State.CARS and self.label.text in cars:
            self.delete()
            self.label.delete()
            Word.point += 1
            print(self.point)
        else:
            Word.point -= 1
            print(self.point)

def create_words():
    word = w.create_sprite(Word)
    word.background(choice(words), 
                    randint(0,w.width), 
                    w.height)

Scheduler.update(create_words, delay=1)
w.run()