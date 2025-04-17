import cv2
import numpy as np
import pyautogui as pg
import matplotlib.pyplot as plt


# take screenshot and store locally 
# screenshot = pg.screenshot('ss.png')

# take a screenshot to locate objects on
screenshot = pg.screenshot()

# adjust colors
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# locate singe object in screenshot
# board = pg.locateOnScreen('googleSearch.png', confidence = 0.9)

# draw rect around object
# cv2.rectangle(
#     screenshot, 
#     (board.left, board.top),
#     (board.left + board.width, board.top + board.height),
#     (0,0,255),
#     2
# )

# detect several objects on screen

for newTab in pg.locateAllOnScreen('newTab.png', confidence=0.7):
    cv2.rectangle(
    screenshot, 
    (newTab.left, newTab.top),
    (newTab.left + newTab.width, newTab.top + newTab.height),
    (0,0,255),
    2
    )

# display screenshot in a window
# cv2.imshow('Screenshot', screenshot)

# # escape condition
# cv2.waitKey(0)

# # clean up windows
# cv2.destroyAllWindows()
plt.imshow(cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR))
plt.title("Screenshot")
plt.axis('off')
plt.show()