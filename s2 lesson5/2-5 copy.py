from pycat.base.color import Color
from pycat.core import Sprite, Window

my_list = [
    'pppppap',
    'pwwwpbw',
    'pwwwpc',
    'pwwwpd',
    'pppppe',
]


tiles = {
    'p':'tiles/tile_000.png',
    'w':'tiles/tile_001.png',
    'a':'tiles/tile_002.png',
    'b':'tiles/tile_003.png',
    'c':'tiles/tile_004.png',
    'd':'tiles/tile_005.png',
    'e':'tiles/tile_006.png',
}



global_image = 'p'
IMAGE_SIZE = 16
PIXEL_SIZE = 100
window = Window(width=len(my_list[0])*PIXEL_SIZE + 200, height=len(my_list)*PIXEL_SIZE, is_sharp_pixel_scaling=True)

class ColorChoice(Sprite):

    def on_create(self):
        self.scale = PIXEL_SIZE/IMAGE_SIZE/2

    def on_left_click(self):
        global global_image
        global_image = self.image
        
        

class Pixel(Sprite):

    def on_create(self):
        self.scale = PIXEL_SIZE/IMAGE_SIZE

    def on_left_click(self):
        global global_image
        self.image = global_image


for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        c = window.create_sprite(Pixel)
        c.x = PIXEL_SIZE/2 + PIXEL_SIZE*j
        c.y = window.height - PIXEL_SIZE/2 - PIXEL_SIZE*i
        c.image = tiles[my_list[i][j]]

for key in tiles.items():
    t = window.create_sprite(ColorChoice)
    t.image = key

window.run()