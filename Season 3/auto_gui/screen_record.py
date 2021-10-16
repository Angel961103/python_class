import cv2
import numpy as np
import pyautogui
from os.path import dirname

cookie = pyautogui.locateOnScreen(dirname(__file__)+"/popcat2.PNG", confidence=0.7)
# display screen resolution, get it from your OS settings
SCREEN_SIZE = (cookie[2], cookie[3])
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

cat = pyautogui.locateOnScreen(dirname(__file__)+"/popcat.PNG", confidence=0.7)

while True:
    # make a screenshot
    img = pyautogui.screenshot(region=cookie)
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # write the frame
    out.write(frame)
    pyautogui.click(cat[0], cat[1])
    # show the frame
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()

