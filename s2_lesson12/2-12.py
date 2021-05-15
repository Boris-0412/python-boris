from enum import Enum
from pycat.base.color import Color
from pycat.core import Window, Scheduler, Label
from pycat.sprite import Sprite
from random import randint, choice
from os import path
from get_data import get_data, write_data

w = Window(enforce_window_limits=False)
folder = path.dirname(__file__)
sports_file = folder+"/sports.txt"
cars_file = folder+"/cars.txt"
animals_file = folder+"/animals.txt"
lines = get_data(sports_file)
print(lines)
    
sports = get_data(sports_file)
cars = get_data(cars_file)
animals = get_data(animals_file)
words = sports + cars + animals

class Score(Label):
    
    def on_create(self):
        self.current = 0
        self.x = w.width/2
        self.file = path.dirname(__file__)+"/highscore.txt"
        self.high = int(get_data(self.file)[0])
        self.text = "High Score: "+ str(self.high)

    def check_high(self):
        if self.current > self.high:
            self.high = self.current
            self.text = "High Score: "+ str(self.high)
            write_data(self.file, str(self.high))
    
score = w.create_label(Score)

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

    def add_point(self):
        self.delete()
        self.label.delete()
        score.current += 1
        score.check_high()
        print(score.current)

    def on_left_click(self):
        if current_state == State.ANIMALS and self.label.text in animals:
            self.add_point()
        elif current_state == State.SPORTS and self.label.text in sports:
            self.add_point()
        elif current_state == State.CARS and self.label.text in cars:
            self.add_point()
        else:
            score.current -=1
            print(score.current)

def create_words():
    word = w.create_sprite(Word)
    word.background(choice(words), 
                    randint(0,w.width), 
                    w.height)

Scheduler.update(create_words, delay=1)
w.run()