from pycat.core import Window,Sprite,Label

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

likes=[]
dislikes=[]

text_label = Label('', 100, 50)

image_number = 0
window = Window(width=1000)
window.background_image = images[image_number]

def next_or_quit():
        global image_number
        image_number+=1
        if image_number>=len(images):
            window.close()
            return
        window.background_image=images[image_number]
        text_label.text = texts[image_number]


class Like(Sprite):
    def on_create(self):
        self.image="thumbs_up.png"
        self.x=800
        self.y=100
        self.scale=0.3
    def on_left_click(self):
        likes.append(texts[image_number])
        print("likes:",likes)
        next_or_quit()

class Dislike(Sprite):
    def on_create(self):
        self.image="thumbs_up.png"
        self.x=600
        self.y=100
        self.scale=0.3
        self.rotation=180
    def on_left_click(self):
        dislikes.append(texts[image_number])
        print("dislikes:",dislikes)
        next_or_quit()

text_label.text = texts[image_number]
window.add_label(text_label)
window.create_sprite(Like)
window.create_sprite(Dislike)
window.run()