from pycat.window import Window
from pycat.sprite import Sprite
from pycat.core import Player, AudioLoop
import random
audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
audio_loop.play()
select_sprite_sound = Player('hit.wav')
match_sprite_sound = Player('point.wav')
no_match_sprite_sound = Player('laugh.wav')


window=Window(background_image="forest_04.png",draw_sprite_rects=True)

clicked_sprite=[]
left=2*[1,2,3,4]
class Card(Sprite):

    def on_create(self):
        self.is_visible=False
        self.is_rotating=False

    def on_left_click(self):
        if self not in clicked_sprite:
            if len(clicked_sprite)<2:
                select_sprite_sound.play()
                clicked_sprite.append(self)
                self.is_visible=True
        
    def on_update(self, dt):
        if self.is_rotating:
            self.rotation += 2
            self.scale -= 0.005
            if self.rotation == 360:
                self.delete()
                left.pop()
                print(len(left))
                if len(left)==0:
                    window.create_sprite(Win,x=500,y=500,scale=2,image='win.png')
                    window.draw_sprite_rects = False
                    a.delete()


left=4*[1,2,3,4]


class Button(Sprite):

    def on_create(self):
        self.image="button.png"
        self.scale=0.75
    def on_left_click(self):
        if len(clicked_sprite)==2:
            sprite1: Sprite =clicked_sprite[0]
            sprite2: Sprite =clicked_sprite[1]
            if sprite1.image==sprite2.image:
                match_sprite_sound.play()
                sprite1.is_rotating=True
                sprite2.is_rotating=True
            else:
                no_match_sprite_sound.play()
                sprite1.is_visible=False
                sprite2.is_visible=False
            clicked_sprite.clear()
        



class Win(Sprite):

    def on_create(self):
        pass
    def on_update(self, dt):
        pass

avatar=4*['avatar_01.png','avatar_02.png','avatar_03.png','avatar_04.png',]
random.shuffle(avatar)
for x in range(100,500,100):
    for y in range(100,500,100):
        window.create_sprite(Card, x=x, y=y, image=avatar.pop())



a=window.create_sprite(Button,x=800,y=200,image='button.png')


window.run()