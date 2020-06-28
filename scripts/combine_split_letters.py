import os
import re

maleLetterCounts = {}
femaleLetterCounts = {}

rootdir = '/home/mforkin/LOR/data/all-split'
for subdir, dirs, files in os.walk(rootdir + os.sep + 'male'):
    for file in files:
        name = re.search("^([0-9]+[a-zA-Z])_*[0-9]*-", file).group(1)
        if name in maleLetterCounts:
            maleLetterCounts[name] = maleLetterCounts[name] + 1
        else:
            maleLetterCounts[name] = 1

for subdir, dirs, files in os.walk(rootdir + os.sep + 'female'):
    for file in files:
        name = re.search("^([0-9]+[a-zA-Z])_*[0-9]*-", file).group(1)
        if name in femaleLetterCounts:
            femaleLetterCounts[name] = femaleLetterCounts[name] + 1
        else:
            femaleLetterCounts[name] = 1

totMales = len(maleLetterCounts)
totFemales = len(femaleLetterCounts)

totMultiMale = len([m for m in maleLetterCounts if maleLetterCounts[m] > 1])
totMultiFemale = len([m for m in femaleLetterCounts if femaleLetterCounts[m] > 1])

print('totMales ' + str(totMales))
print('multiPageMales: ' + str(totMultiMale))
print('multiMalePercent: ' + str(totMultiMale / totMales)) #30.3%

print('totMales ' + str(totFemales))
print('multiPageFemales: ' + str(totMultiFemale))
print('multiFemalePercent: ' + str(totMultiFemale / totFemales)) #30.7%



