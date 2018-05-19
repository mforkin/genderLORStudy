from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import subprocess
#import sys

#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/bin/')
#import pdf2txt

rootdir = '/Users/mike/resumeData'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if subdir.endswith("pages"):
            filepath = subdir + os.sep + file
            txtFPath = subdir[0:-5] + "txt" + os.sep + file[0:-4] + ".txt"

            if filepath.endswith(".pdf"):
                #print(filepath)
                #print(txtFPath)
                proc = subprocess.Popen(["bash", "-c", "python3.7 /Library/Frameworks/Python.framework/Versions/3.7/bin/pdf2txt.py '" + filepath + "' >> '" + txtFPath + "'"])
                #txt = proc.communicate()[0].decode('utf-8')
                #print(txt)
