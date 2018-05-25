import os
import re
import subprocess
#import sys

rootdir = '/Users/mike/resumeData'

males = set() 
females = set() 
unsure = set()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        pagesValid = False
        #print os.path.join(subdir, file)
        if subdir.endswith("txt"):
            filepath = subdir + os.sep + file
            if filepath.endswith(".txt"):
                name = "_".join(filepath.split("_")[0:2])
                numHes = 0
                numShes = 0
                numHis = 0
                numHer = 0
                if name in males:
                    numHes = 1
                elif name in females:
                    numShes = 1
                else:
                    with open(filepath) as f:
                        content = f.read()
                        numHes = len(re.findall(" he ", content))
                        numShes = len(re.findall(" she ", content))
                        numHis = len(re.findall(" his ", content))
                        numHer = len(re.findall(" her ", content))
                if (numHes + numHis) > (numShes + numHer):
                    os.rename(filepath, subdir + os.sep + "male" + os.sep + file)
                    males.add(name)
                elif (numShes + numHer) > (numHes + numHis):
                    os.rename(filepath, subdir + os.sep + "female" + os.sep + file)
                    females.add(name) 
                else:
                    unsure.add(name)

print("Males: %s" % len(males))
print("females: %s" % len(females))
print("unsure: %s" % len(unsure))

