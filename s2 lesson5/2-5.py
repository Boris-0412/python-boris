from pycat.base.color import Color
from pycat.core import Sprite, Window

my_list = [
    'ppppp',
    'pwpwp',
    'pprpp',
    'ppppp',
    'pbbbp',
]


colors = {
    'p':Color.PURPLE,
    'w':Color.WHITE,
    'r':Color.RED,
    'b':Color.BLACK,
}


PIXEL_SIZE = 100
window = Window(width=len(my_list[0])*PIXEL_SIZE, height=len(my_list)*PIXEL_SIZE)

class Pixel(Sprite):

    def on_create(self):
        self.scale = PIXEL_SIZE


for i in range(len(my_list)):
    for j in range(len(my_list[0])):
        c = window.create_sprite(Pixel)
        c.x = PIXEL_SIZE/2 + PIXEL_SIZE*j
        c.y = window.height - PIXEL_SIZE/2 - PIXEL_SIZE*i
        c.color = colors[my_list[i][j]]
            
            

    
window.run()