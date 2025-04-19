import cv2
import numpy as np
import pyautogui as pg
import time

import pytesseract
from PIL import Image
import array as arr
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

MAX_CONFIDENCE = 1.0

def findConfidence(img): # find the confidence of the image
    con = 0.5
    foundCon = None
    while con <= MAX_CONFIDENCE:
        try:
            res = pg.locateOnScreen(img, confidence=con)
            if res:
                con += 0.1
            else:
                con -= 0.1
                foundCon = con
        except IOError as e:
            # print("I/O ERROR OCCURRED:", e)
            break
        except Exception as e:
            print("Unexpected error:", img)
            con -= 0.1
            foundCon = con
            break
    return foundCon

def moveToImage(locatedImg): # move the mouse to that position
    if locatedImg:
        pg.moveTo(locatedImg.left + (locatedImg.width//2), locatedImg.top + (locatedImg.height//2), duration = 1)
        pg.click()

def newScreenshot(sleepTime): # take a new screenshot
    time.sleep(sleepTime)
    return pg.screenshot()

def readScreenshot(word, sleepTime): # reads the screenshot
    screenshot = newScreenshot(sleepTime)
    matchedRows = allInstancesOfWord(screenshotInfo(screenshot), word)
    firstOp = matchedRows[0]
    pg.moveTo(int(firstOp['left']) + (int(firstOp['width'])//2), int(firstOp['top']) + (int(firstOp['height'])//2), duration = 1)
    pg.click()

def screenshotInfo(screenshot): # finds all info in the screenshot
    return pytesseract.image_to_data(screenshot, lang = 'eng', output_type=Output.DICT)

def allInstancesOfWord(data, word): # finds all instances of the word
    matchedRows = []
    for i in range(len(data['text'])):
        if data['text'][i].strip().lower() == word.lower():
            row = {key: data[key][i] for key in data}
            matchedRows.append(row)

    return matchedRows
