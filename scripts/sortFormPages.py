import os
import re

rootdir = '/home/mforkin/LOR/data/all-split'

sort_col = 'gender'

unsure = set()
forms1 = set()
forms2 = set()

i = 0

for subdir, dirs, files in os.walk(rootdir):
    if subdir is rootdir:
        for file in files:
            if file.endswith(".txt"):
                filepath = subdir + os.sep + file
                name = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
                page1 = "Nature and amount of contact with the applicant"
                page2 = "If you worked with this applicant in a clinical setting, what grade would you assign"
                with open(filepath) as f:
                    content = f.read()
                    page1cnt = len(re.findall(page1, content))
                    page2cnt = len(re.findall(page2, content))
                if (page1cnt > 0):
                    os.rename(filepath, subdir + os.sep + "form1" + os.sep + file)
                    forms1.add(name)
                elif (page2cnt > 0):
                    os.rename(filepath, subdir + os.sep + "form2" + os.sep + file)
                    forms2.add(name)
                else:
                    unsure.add(name)

print("Males: %s" % len(forms1))
print("females: %s" % len(forms2))
print("unsure: %s" % len(unsure))