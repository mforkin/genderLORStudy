import pandas as pd
import os
import glob
import re

rootdir = '/home/mforkin/LOR/data/all-split'

keyfile = '/home/mforkin/LOR/data/key.csv'

data = pd.read_csv(keyfile)

correct = 0
incorrect = 0
seen = set()
incorrectFiles = set()

for i, r in data.iterrows():
    id = r['Participant Number']
    gender = r['Gender']
    if not id in seen:
        seen.add(id)
        correctGenderFiles = glob.glob(rootdir + os.sep + gender.lower() + os.sep + "*")
        correct += len([name for name in correctGenderFiles if re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", name.split(os.sep)[-1]).group(1) == str(id)])
        iGender = 'male'
        if gender.lower() == 'male':
            iGender = 'female'
        inCorrectGenderFiles = glob.glob(rootdir + os.sep + iGender.lower() + os.sep + "*")
        numIncorrect = len([name for name in inCorrectGenderFiles if re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", name.split(os.sep)[-1]).group(1) == str(id)])
        incorrect += numIncorrect
        if numIncorrect > 0:
            incorrectFiles.add(id)

print("correct: %s" %correct)
print("incorrect: %s" %incorrect)
print("incorrect files: ---------------")
print(incorrectFiles)




