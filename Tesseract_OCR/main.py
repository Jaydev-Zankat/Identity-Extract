import pytesseract
from PIL import Image

img_file = "./icard_5.png"
img = Image.open(img_file)
ocr_result = pytesseract.image_to_string(img)
print (ocr_result)

img_box = pytesseract.image_to_boxes(img)
print(img_box)