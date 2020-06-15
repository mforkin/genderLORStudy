import os
from PIL import Image
import pytesseract

rootdir = "/home/mforkin/LOR/data/all-split"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.jpg'):
            filePath = rootdir + os.sep + file
            txtPath = rootdir + os.sep + file[0:-8] + '.txt'
            txt = pytesseract.image_to_string(Image.open(filePath))
            with open(txtPath, 'w') as wf:
                wf.write(txt)