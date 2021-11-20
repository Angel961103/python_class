from pycat.base.color import Color
from pycat.core import Window
from typing import List

from pycat.sprite import Sprite

w = Window()

class Button(Sprite):
    def on_create(self):
        self.scale = 50
        self.color = Color.AMBER
        self.message = ""
        self.node = None
        self.label = None

    def set_message(self, x:int, y:int, msg: str, node: 'Node'):
        self.message = msg
        self.node = node
        self.label = w.create_label(text=msg)
        self.x = x
        self.y = y
        self.label.x = self.x + self.width
        self.label.y = self.y + self.label.content_height/2

    def on_left_click(self):
        global current_node
        current_node.hide()
        current_node = self.node
        current_node.show()

    def delete(self):
        self.label.delete()
        super().delete()

class Node:
    def __init__(self, name: str, img: str):
        self.room_name = name
        self.background = w.create_sprite(image=img)
        self.background.position = w.center
        self.background.is_visible = False
        self.neighbors: List[Node] = []
        self.buttons: List[Button] = []
        self.messages:List[str] = []
        print("node created")

    def add_path(self, node: "Node", msg: str):
        self.neighbors.append(node)
        self.messages.append(msg)

    def create_button(self, msg: str, node: 'Node'):
        print(msg)
        b = w.create_sprite(Button)
        y = 100*len(self.buttons) + 100
        b.set_message(100, y, msg, node)
        self.buttons.append(b)


    def show(self):
        self.background.is_visible = True
        for i in range(len(self.neighbors)):
            self.create_button(self.messages[i], self.neighbors[i])

    def hide(self):
        self.background.is_visible = False
        for b in self.buttons:
            b.delete()
        self.buttons.clear()


castle = Node(name="Castle", img="Castle.PNG")
inside_castle = Node(name="inside_castle", img="Castle_inside.PNG")
field = Node(name="field", img="field.PNG")

field.add_path(castle, "go back to castle")

castle.add_path(inside_castle, "go inside")
castle.add_path(field, "go to field")

castle.show()
current_node = castle

w.run()