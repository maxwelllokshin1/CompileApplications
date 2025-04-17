import cv2
import numpy as np
import pyautogui as pg
import time

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

MAX_CONFIDENCE = 1.0

def findConfidence(img):
    con = 0.1
    foundCon = None
    while con <= MAX_CONFIDENCE:
        try:
            res = pg.locateOnScreen(img, confidence=con)
            if res:
                print(f"Image found at: {con}")
                con += 0.1
            else:
                print(f"Not found at {con}, increasing...")
                con -= 0.1
                foundCon = con
        except IOError as e:
            print("I/O ERROR OCCURRED:", e)
            break
        except Exception as e:
            print("Unexpected error:", e)
            print(f"Not found at {con}")
            con -= 0.1
            foundCon = con
            break
    return foundCon

def moveToOpp(locatedImg):
    if locatedImg:
        pg.moveTo(locatedImg.left + (locatedImg.width//2), locatedImg.top + (locatedImg.height//2), duration = 1)
        pg.click()

def newScreenshot():
    time.sleep(1)
    return pg.screenshot()

def cropScreenshot(x, y, width, height):
    screenshot = newScreenshot()
    # crop_box = (x, y, x + width, y + height)

    # # Crop the image
    # cropped_image = screenshot.crop(crop_box)

    # # Save or display the cropped image

    # # cropped_image.save("cropped.png")
    screenshot.show()
    printAllInfo(screenshot)

def printAllInfo(screenshot):
    print(pytesseract.image_to_data(screenshot, lang = 'eng'))


