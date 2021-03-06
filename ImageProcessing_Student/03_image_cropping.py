from pycat.core import Window, Sprite
from pycat.base import NumpyImage as Image
import os 
import random

def load_images(img_dir: str):
    face_images = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_dir_path = dir_path + "/" + img_dir
    for file in os.listdir(img_dir_path):
        filepath = img_dir_path + file
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
            face_images.append(img_dir + "/" + file)
    return face_images

face=load_images("resized_faces")
print(face)

window = Window()
original_image = Image.get_array_from_file(random.choice(face))
print(original_image.shape)
rows, cols, channels = original_image.shape

class MyCustomSprite(Sprite):

    def on_create(self):
        self.i0 = 0
        self.i1 = 0
        self.j0 = 0
        self.j1 = 0

    def on_update(self, dt):
        pass

    def set_range(self,i0,i1,j0,j1):
        self.i0 = i0
        self.i1 = i1
        self.j0 = j0
        self.j1 = j1

    def on_left_click(self):
        original_image = Image.get_array_from_file(random.choice(face))

        image = original_image[self.i0:self.i1, self.j0:self.j1, :]
        self.texture = Image.get_texture_from_array(image)





left_eye_image = original_image[50:70, 20:40, :]
left_eye = window.create_sprite(MyCustomSprite)
left_eye.set_range(50,70, 20,40)
left_eye.position = (500, 500)
left_eye.texture = Image.get_texture_from_array(left_eye_image)
left_eye.scale = 10
original_image = Image.get_array_from_file(random.choice(face))

right_eye_image = original_image[50:70, 60:80, :]
right_eye = window.create_sprite(MyCustomSprite)
right_eye.set_range(50,70, 60,80)
right_eye.position = (700, 500)
right_eye.texture = Image.get_texture_from_array(right_eye_image)
right_eye.scale = 10
original_image = Image.get_array_from_file(random.choice(face))

nose_image = original_image[27:50, 33:63, :]
nose = window.create_sprite(MyCustomSprite)
nose.set_range(27,50, 33,63)
nose.position = (600, 330)
nose.texture = Image.get_texture_from_array(nose_image)
nose.scale = 6
original_image = Image.get_array_from_file(random.choice(face))

mouth_image = original_image[10:30, 25:70, :]
mouth = window.create_sprite(MyCustomSprite)
mouth.set_range(10,30, 25,70)
mouth.position = (600, 200)
mouth.texture = Image.get_texture_from_array(mouth_image)
mouth.scale = 6



window.run()