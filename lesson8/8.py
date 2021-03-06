from pycat.window import Window
from pycat.sprite import Sprite
window=Window(background_image="img/forest_04.png", draw_sprite_rects=True)

clicked_sprites=[]
class Card(Sprite):
    def on_create(self):
        self.is_visible=False
    def on_left_click(self):
        
        
        if len(clicked_sprites) < 2:
            if self not in clicked_sprites:
                clicked_sprites.append(self)
                self.is_visible=True
                

class Button(Sprite):
     def on_create(self):
         self.image="img/button.png"
         self.x=600
         self.y=300
         self.scale=0.5
     def on_left_click(self):
        print(clicked_sprites)
        sprite1: Sprite=clicked_sprites[0]
        sprite2: Sprite=clicked_sprites[1]

        if sprite1.image == sprite2.image:
            sprite1.delete()
            sprite2.delete()
        else:
            sprite1.is_visible=False
            sprite2.is_visible=False
        clicked_sprites.clear()
            

window.create_sprite(Card,x=100 ,y=100, image="img/avatar_01.png")
window.create_sprite(Card,x=100 ,y=200, image="img/avatar_03.png")
window.create_sprite(Card,x=200 ,y=100, image="img/avatar_03.png")
window.create_sprite(Card,x=200 ,y=200, image="img/avatar_01.png")
window.create_sprite(Card,x=300 ,y=100, image="img/avatar_04.png")
window.create_sprite(Card,x=300 ,y=200, image="img/avatar_04.png")
window.create_sprite(Card,x=300 ,y=300, image="img/avatar_02.png")
window.create_sprite(Card,x=300 ,y=400, image="img/avatar_01.png")
window.create_sprite(Card,x=100 ,y=400, image="img/avatar_04.png")
window.create_sprite(Card,x=400 ,y=400, image="img/avatar_02.png")
window.create_sprite(Card,x=400 ,y=100, image="img/avatar_01.png")
window.create_sprite(Card,x=400 ,y=200, image="img/avatar_02.png")
window.create_sprite(Card,x=400 ,y=300, image="img/avatar_03.png")
window.create_sprite(Card,x=100 ,y=300, image="img/avatar_02.png")
window.create_sprite(Card,x=200 ,y=400, image="img/avatar_04.png")
window.create_sprite(Card,x=200 ,y=300, image="img/avatar_03.png")





window.create_sprite(Button)

window.run()


 