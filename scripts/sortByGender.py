import os
import re
import subprocess
#import sys

rootdir = '/Users/mike/resumeData'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pagesValid = False
        #print os.path.join(subdir, file)
        if subdir.endswith("txt"):
            filepath = subdir + os.sep + file
            if filepath.endswith(".txt"):
                numHes = 0
                numShes = 0
                with open(filepath) as f:
                    content = f.read()
                    numHes = len(re.findall(" he ", content))
                    numShes = len(re.findall(" she ", content))
                if numHes > numShes:
                    print(os.rename(filepath, subdir + os.sep + "male" + os.sep + file))
                elif numShes > numHes:
                    print(os.rename(filepath, subdir + os.sep + "female" + os.sep + file))	
