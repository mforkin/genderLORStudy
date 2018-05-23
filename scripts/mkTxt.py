import os
import subprocess
from PIL import Image
import pytesseract
#import sys


rootdir = '/Users/mike/resumeData'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if subdir.endswith("pages"):
            filepath = subdir + os.sep + file
            txtFPath = subdir[0:-5] + "txt" + os.sep + file[0:-5] + ".txt"

            if filepath.endswith(".jpg"):
                txt = pytesseract.image_to_string(Image.open(filepath))
                with open(txtFPath, 'w') as wf:
                    wf.write(txt)

