import os
import re

maleLetterCounts = {}
femaleLetterCounts = {}

rootdir = '/home/mforkin/LOR/data/all-split'
for subdir, dirs, files in os.walk(rootdir + os.sep + 'male'):
    for file in files:
        name = re.search("^([0-9]+[a-zA-Z])_*[0-9]*-", file).group(1)
        if name in maleLetterCounts:
            maleLetterCounts[name] = maleLetterCounts[name] + [file]
        else:
            maleLetterCounts[name] = [file]

for subdir, dirs, files in os.walk(rootdir + os.sep + 'female'):
    for file in files:
        name = re.search("^([0-9]+[a-zA-Z])_*[0-9]*-", file).group(1)
        if name in femaleLetterCounts:
            femaleLetterCounts[name] = femaleLetterCounts[name] + [file]
        else:
            femaleLetterCounts[name] = [file]

totMales = len(maleLetterCounts)
totFemales = len(femaleLetterCounts)

totMultiMale = len([m for m in maleLetterCounts if len(maleLetterCounts[m]) > 1])
totMultiFemale = len([m for m in femaleLetterCounts if len(femaleLetterCounts[m]) > 1])

print('totMales ' + str(totMales))
print('multiPageMales: ' + str(totMultiMale))
print('multiMalePercent: ' + str(totMultiMale / totMales)) #30.3%

print('totMales ' + str(totFemales))
print('multiPageFemales: ' + str(totMultiFemale))
print('multiFemalePercent: ' + str(totMultiFemale / totFemales)) #30.7%

# clean headers and footers before joining multiple pages
for m in maleLetterCounts:
    num = len(maleLetterCounts[m])
    if num > 1:
        correct_file = ""
        for f in maleLetterCounts[m]:
            with open(rootdir + os.sep + 'male' + os.sep + f) as inf:
                content = inf.read()
                keeper = len(re.findall("please limit your response to 250 words or less", content))
                if keeper > 0:
                    correct_file = f

        if len(correct_file) == 0:
            if len(maleLetterCounts[m]) == 2:
                f1 = maleLetterCounts[m][0]
                f2 = maleLetterCounts[m][1]
                #if (len(re.findall('page0', f1)) == 0 and len(re.findall('page1', f1)) == 0) or (len(re.findall('page0', f2)) == 0 and len(re.findall('page1', f2)) == 0):
                    #print(f1, f2)
                with open(f1) as f1f:
                    with open(f2) as f2f:
                        name = re.search("^([0-9]+[a-zA-Z])_*[0-9]*-", f1).group(1)
                        print(name)
                        f1_content = f1f.read()
                        f2_content = f2f.read()
        else:
            for f in maleLetterCounts[m]:
                if f is correct_file:
                    print('keeping ' + f + '\n')
                else:
                    print('removing ' + f + '\n')
                    os.rename(rootdir + os.sep + 'male' + os.sep + f, rootdir + os.sep + 'form_other' + os.sep + f)

