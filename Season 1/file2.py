from pycat.window import Window
from test.support import bigaddrspacetest
window = Window()

animal=input("Please enter the animal you want to see:")
size=input("Do you want your animal to be big or small or not?")
left=input("Do you want your animal at left or right or not?")
point=input("Do you want your animal point left or right?")
print("here is your animal.")
animal_png=window.create_sprite()
animal_png.x=animal_png.x+650
animal_png.y=animal_png.y+300
if animal=="elephant":
    animal_png.image="elephant.png"
if animal=="owl":
    animal_png.image="owl.gif"
if size=="big":
    animal_png.scale =2
if size=="small":
    animal_png.scale =0.5
if left=="left":
    animal_png.x=-100
if left=="right":
    animal_png.x=+100
if point=="left":
    animal_png.scale_x=-1
window.run()