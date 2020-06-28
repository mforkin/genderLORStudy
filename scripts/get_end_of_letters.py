import os
import re

rootdir = '/home/mforkin/LOR/data/all-split'


femaleIds = {}
maleIds = {}

males = 0
females = 0
unknown = 0

for subdir, dir, files in os.walk(rootdir + os.sep + 'female'):
    for file in files:
        if file.endswith('.txt'):
            name = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
            if name in femaleIds:
                femaleIds[name] = femaleIds[name] + 1
            else:
                    femaleIds[name] = 1

for subdir, dir, files in os.walk(rootdir + os.sep + 'male'):
    for file in files:
        if file.endswith('.txt'):
            name = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
            if name in maleIds:
                maleIds[name] = maleIds[name] + 1
            else:
                maleIds[name] = 1

for subdir, dirs, files in os.walk(rootdir):
    if subdir is rootdir:
        for file in files:
            if file.endswith('.txt'):
                filepath = subdir + os.sep + file
                name = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
                if name in femaleIds and not name in maleIds:
                    females = females + 1
                    os.rename(filepath, subdir + os.sep + 'female' + os.sep + file)
                elif name in maleIds and not name in femaleIds:
                    males = males + 1
                    os.rename(filepath, subdir + os.sep + 'male' + os.sep + file)
                elif femaleIds[name] > maleIds[name]:
                    females = females + 1
                    os.rename(filepath, subdir + os.sep + 'female' + os.sep + file)
                elif maleIds[name] > femaleIds[name]:
                    males = males + 1
                    os.rename(filepath, subdir + os.sep + 'male' + os.sep + file)
                else:
                    unknown = unknown + 1

print('unknown: ' + str(unknown))
print('males ' + str(males))
print('females ' + str(females))


