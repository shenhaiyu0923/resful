#coding:utf-8
from PIL import Image
import pytesseract


# im = Image.open('test.jpg')
im = Image.open('123.png')

result = pytesseract.image_to_string(im)#不识别中文
print(result)