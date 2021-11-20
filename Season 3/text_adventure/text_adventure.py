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

class Player:
    def __init__(self):
        self.items : List[Item] = []
        
player = Player()



class Item(Sprite):
    def on_create(self):
        self.name = ""
        self.node = None
        self.is_visible = False

    def on_left_click(self):
        player.items.append(self)
        self.node.remove_item(self)
        

class Node:
    def __init__(self, name: str, img: str):
        self.name = name
        self.background = w.create_sprite(image=img)
        self.background.position = w.center
        self.background.is_visible = False
        self.neighbors: List[Node] = []
        self.buttons: List[Button] = []
        self.messages:List[str] = []
        self.items: List[Item] = []
        print("node created")

    def add_path(self, node: "Node", msg: str):
        self.neighbors.append(node)
        self.messages.append(msg)

    def add_item(self, item: Item):
        self.items.append(item)
        item.node = self

    def remove_item(self, item: Item):
        self.items.remove(item)
        item.node = None
        item.is_visible = False
        for i in range(len(self.neighbors)):
            node = self.neighbors[i]
            if isinstance(node, SceretNode):
                if node.required_item in player.items:
                    self.create_button(self.messages[i], node)


    def create_button(self, msg: str, node: 'Node'):
        print(msg)
        b = w.create_sprite(Button)
        y = 100*len(self.buttons) + 100
        b.set_message(100, y, msg, node)
        self.buttons.append(b)


    def show(self):
        self.background.is_visible = True
        for item in self.items:
            item.is_visible = True
        
        for i in range(len(self.neighbors)):
            node = self.neighbors[i]
            if isinstance(node, SceretNode):
                if node.required_item in player.items:
                    self.create_button(self.messages[i], node)

            else:
                self.create_button(self.messages[i], node)

    def hide(self):
        self.background.is_visible = False
        for b in self.buttons:
            b.delete()
        self.buttons.clear()
        for item in self.items:
            item.is_visible = False

class SceretNode(Node):
    def __init__(self, name: str, img: str, required_item: Item):
        super().__init__(name, img)
        self.required_item = required_item



key = w.create_sprite(Item, image="key.PNG", scale=0.3, x=600, y=200, layer=5)
castle = Node(name="Castle", img="Castle.PNG")
inside_castle = Node(name="inside_castle", img="Castle_inside.PNG")
field = Node(name="field", img="field.PNG")
room = SceretNode(name="room", img="room.PNG", required_item=key)

field.add_path(castle, "go back to castle")

inside_castle.add_path(room, "go to the room")
inside_castle.add_item(key)

castle.add_path(inside_castle, "go inside")
castle.add_path(field, "go to field")

castle.show()
current_node = castle

w.run()