import pyautogui as pg
import cv2
import numpy as np
import time
import locate
import pyperclip as pc


def checkIfTabAlreadyOpen(steps):
    for i, img in enumerate(reversed(steps), 1):
        count = len(steps) - i+1
        res = tryMoveToImage(img, count)
        if res is not None:
            return res
        if img == 'cvImgs/googleSearch.png':
            res = tryMoveToImage('cvImgs/newTab.png', count)
            if res is not None:
                return res
        count-=1
    print('--------------------')
    return count

def tryMoveToImage(img, returnValue):
    con = locate.findConfidence(img)
    if con > 0.8:
        print(img)
        try:
            locate.moveToImage(pg.locateOnScreen(img, confidence=con))
            return returnValue
        except Exception as e:
            print("Unexpected error:", img)
    return None


def navSteps(steps, watchFor):
    for img in range(checkIfTabAlreadyOpen(steps), len(steps)):
        locate.moveToImage(pg.locateOnScreen(steps[img], confidence=locate.findConfidence(steps[img])))
        if steps[img] == watchFor:
            print('HI')
            copyAndPaste("google")

def copyAndPaste(word):
    pc.copy(word)
    pg.hotkey("ctrl", "v")
    time.sleep(1)
    pg.press("enter")

def main():
    steps = ['cvImgs/windowsSearch.png',  
         'cvImgs/googleSearch.png']
    navSteps(steps, 'cvImgs/windowsSearch.png')

    copyAndPaste('gmail')

    locate.readScreenshot('email', 1)
    time.sleep(3)
    steps = ['cvImgs/magGlass.png']
    navSteps(steps, None)
    copyAndPaste('no-reply')


if __name__ == "__main__":
    main()