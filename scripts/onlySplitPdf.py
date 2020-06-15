from PyPDF2 import PdfFileWriter, PdfFileReader
import os


rootdir = '/home/mforkin/LOR/data/all'
outdir = '/home/mforkin/LOR/data/all-split'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.pdf') and not file.startswith('.'):
            pdfInputPath = rootdir + os.sep + file
            inputpdf = PdfFileReader(open(pdfInputPath, 'rb'))
            for i in iter(range(inputpdf.numPages)):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                fname = outdir + os.sep + file[0:-4] + "-page%s.pdf" %i
                with open(fname, 'wb') as outputStream:
                    output.write(outputStream)
