import pyautogui as gui
from os.path import dirname

cat = gui.locateOnScreen(dirname(__file__)+"/popcat.PNG", confidence=0.7)


if cat:
    for i in range(100):
        gui.click(cat[0], cat[1])