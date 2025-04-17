import pandas as pd
import numpy as np

from glob import glob
from tqdm.notebook import tqdm

import matplotlib.pyplot as plt
from PIL import Image

plt.style.use('ggplot')

# outline
# 1. take look at data
# 2. extract text from image
#       - pytesseract
#       - easyocr
#       - keras_ocr
# 3. run on a few examples and compare the results

annot = pd.read_parquet('annot.parquet')
imgs = pd.read_parquet('img.parquet')
img_fns = glob('train_val_images/train_images/*')
# annot.head()

# plt.imshow(plt.imread(img_fns[0]))
# plt.title("Screenshot")
# plt.axis('off')
# plt.show()

# image_id = img_fns[1].split('/')[-1].split('.')[0] # gets the image id

# fig, ax = plt.subplots(figsize=(10,10))
# plt.imshow(plt.imread(img_fns[1]))
# plt.show()
# annot.query('image_id == @image_id')

# fig,axs = plt.subplots(5,5, figsize=(20,20))
# axs = axs.flatten()
# for i in range(25):
#     axs[i].imshow(plt.imread(img_fns[i]))
#     axs[i].axis('off')
#     image_id = img_fns[i].split('/')[-1].rstrip('.jpg')
#     n_annot = len(annot.query('image_id == @image_id'))
#     axs[i].set_title(f'{image_id} - {n_annot}')
# plt.show()

# first method using pytesseract

import pytesseract
#example call

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
print(pytesseract.image_to_string(img_fns[11], lang = 'eng'))