from pycat.core import Window ,Sprite ,Color
from pycat.label import Label

w = Window()

class Cell(Sprite):

    def on_create(self):
        self.height = 80
        self.width = 80
        self.color = Color.RED

    def create_label(self ,value):
        self.value = value
        self.label = w.create_label()
        self.label.text = str(value)
        self.label.x = self.x 
        self.label.y = self.y

    def set_color(self, max, min):
        scale = (self.value - min)/(max-min)
        self.color = Color(255, (1-scale)*255,(1-scale)*255)

my_list = [
    [1 ,2 ,3 ,4],
    [5 ,6 ,7 ,8],
    [9 ,10, 11, 12]
]

list_min = list_max = my_list[0][0]
for i in range(3):
    for j in range(4):
        v = my_list[i][j]
        if v < list_min:
            list_min = v
        if v > list_max:
            list_max = v
print(list_min, list_max)

for i in range(3):
    for j in range(4):
        #print(my_list[i][j], end=" ")
        # label_1 = w.create_label()
        # label_1.text = str(my_list[i][j])
        # label_1.x = 100 + j*50
        # label_1.y = w.height - i*50
        cell = w.create_sprite(Cell)
        cell.x = 600 + j*(cell.width+1)
        cell.y = w.height - 300 - i*(cell.height+1)
        cell.create_label(my_list[i][j])
        cell.set_color(list_max, list_min)

w.run()