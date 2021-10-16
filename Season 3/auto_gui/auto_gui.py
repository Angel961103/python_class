import pyautogui as gui
from os.path import dirname

cookie = gui.locateOnScreen(dirname(__file__)+"/Capture.PNG", confidence=0.7)


if cookie:
    for i in range(10):
        gui.click(cookie[0], cookie[1])

grandma = gui.locateOnScreen(dirname(__file__)+"/Grandma.PNG", confidence=0.7)

if grandma:
    gui.click(grandma[0], grandma[1])
