__author__ = u'james.morris'
import os

try:
    import Image

except ImportError:
    from PIL import Image

import pytesseract

fileImage = os.getcwd() + os.sep + u"example.png"

print(u"%s" % fileImage)

text = pytesseract.image_to_string(Image.open(fileImage))

print(u"Text[%d] : %s" % (len(text), text))

# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
