from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import subprocess
#import sys

#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/bin/')
#import pdf2txt

rootdir = '/Users/mike/resumeData'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pagesValid = False
        #print os.path.join(subdir, file)
        if not subdir.endswith("pages"):
            filepath = subdir + os.sep + file
    
            if filepath.endswith(".pdf"):
                inputpdf = PdfFileReader(open(filepath, "rb"))
                for i in iter(range(inputpdf.numPages)):
                    output = PdfFileWriter()
                    output.addPage(inputpdf.getPage(i))
                    #print(subdir + "-pages" + os.sep + file[0:-4] + "-page%s.pdf" % i)
                    fname = subdir + "-pages" + os.sep + file[0:-4] + "-page%s.pdf" % i
                    with open(fname, "wb") as outputStream:
                        output.write(outputStream)
                    if not pagesValid:
                        print (fname)
                        proc = subprocess.Popen(["bash", "-c", "python3.7 /Library/Frameworks/Python.framework/Versions/3.7/bin/pdf2txt.py '" + fname + "'"], stdout=subprocess.PIPE)
                        txt = proc.communicate()[0].decode('utf-8')
                        #print(txt)
                        os.remove(fname)
                        if 'PHYSICIAN DATA CENTER INFORMATION APPEARING AS NOTE' in txt:
                           pagesValid = True
