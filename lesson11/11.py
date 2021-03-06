from pycat.core import Window,Sprite,Label

texts = [
   'Red squirrel',
   'Pheasant',
   'Sheep',
   'Cow',
   'Seal',
   'Cat',
   'Hedgehog',
   'Meerkat',
]

images = [
   'squirrel.jpg',
   'bird.jpg',
   'sheep.jpg',
   'cow.jpg',
   'seal.jpg',
   'cat.jpg',
   'hedgehog.jpg',
   'meerkat.jpg',
]

likes=[]
dislikes=[]

text_lable = Label('Boris', 100, 50)
image_number = 0
window = Window(width=1000)
window.background_image = images[image_number]
text_lable.text=texts[image_number]



def next():
    global image_number
    image_number+=1
    if image_number < len(images):
        window.background_image = images[image_number]
        text_lable.text=texts[image_number]
    else:
        window.close()

class NextButton(Sprite):

    def on_create(self):
        self.image='button_next.png'
        self.x=800
        self.y=100
        self.scale=0.5
    def on_left_click(self):
        next()

class LikeButton(Sprite):

    def on_create(self):
        self.image = 'thumbs_up.png'
        self.x=550
        self.y=100
        self.scale=0.25

    def on_left_click(self):
        likes.append(texts[image_number])
        print("I like",likes,"!")
        next()

class DisLikeButton(Sprite):

    def on_create(self):
        self.image = 'thumbs_up.png'
        self.rotation = 180
        self.x = 400
        self.y = 100
        self.scale = 0.25
    def on_left_click(self):
        dislikes.append(texts[image_number])
        print("I dislike",dislikes,"!")
        next()

window.add_label(text_lable)
window.create_sprite(NextButton)
window.create_sprite(LikeButton)
window.create_sprite(DisLikeButton)

window.run()















