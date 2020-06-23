import os
import re

rootdir = '/home/mforkin/LOR/data/all-split'

sort_col = 'gender'

males = set()
females = set()
unsure = set()

i = 0

for subdir, dirs, files in os.walk(rootdir):
    if subdir is rootdir:
        for file in files:
            if i % 100 is 0:
                print("processed: %s" % i)
            if file.endswith(".txt"):
                filepath = subdir + os.sep + file
                name = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
                numHes = 0
                numShes = 0
                numHis = 0
                numHer = 0
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

