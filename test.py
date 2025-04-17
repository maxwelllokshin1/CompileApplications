import pytesseract
from PIL import Image
import pyautogui as pg
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

screenshot = pg.screenshot()

# x, y = pg.position()
# width, height = pg.size()

# x = 0
# y = 0
# width = width - x
# height = height - y
# crop_box = (x, y, x + width, y + height)

# # Crop the image
# cropped_image = screenshot.crop(crop_box)

# # Save or display the cropped image
# cropped_image.show()
data = pytesseract.image_to_data(screenshot, lang = 'eng', output_type=Output.DICT)
texts = data['text']

# You can filter out empty strings if needed
filtered_texts = [word for word in texts if word.strip() == 'Email']

print(filtered_texts)

