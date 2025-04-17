import pyautogui as pg
import cv2
import numpy as np
import time
import locate
import pyperclip as pc


steps = ['cvImgs/windowsSearch.png', 
         'cvImgs/googleIcon.png', 
         'cvImgs/googleSearch.png']


def checkIfTabAlreadyOpen():
    for i, img in enumerate(reversed(steps), 1):
        count = len(steps) - i
        print(count)
        res = tryMoveToImage(img, count)
        if res is not None:
            return res
        if img == 'cvImgs/googleSearch.png':
            res = tryMoveToImage('cvImgs/newTab.png', count)
            if res is not None:
                return res
        count-=1

    return count

def tryMoveToImage(img, returnValue):
    con = locate.findConfidence(img)
    if con > 0.8:
        print(img)
        try:
            locate.moveToOpp(pg.locateOnScreen(img, confidence=con))
            return returnValue
        except Exception as e:
            print("Unexpected error:", e)
    return None


def navToGmail():
    for img in range(checkIfTabAlreadyOpen(), len(steps)):
        locate.moveToOpp(pg.locateOnScreen(steps[img], confidence=locate.findConfidence(steps[img])))

def main():
    navToGmail()

    pc.copy("gmail")
    pg.hotkey("ctrl", "v")
    pg.press("enter")
    x, y = pg.position()
    width, height = pg.size()
    pg.moveTo(0, height//8, duration = 1)
    x, y = pg.position()
    locate.cropScreenshot(x,y, (width//4), height//5)


if __name__ == "__main__":
    main()