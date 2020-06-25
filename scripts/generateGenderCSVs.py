import os
import re

rootdir = '/home/mforkin/LOR/data/all-split'

for subdir, dirs, files in os.walk(rootdir + os.sep + 'male'):
    with open(rootdir + os.sep + 'bigTxtMale' + os.sep + 'data.csv', 'w') as out:
        out.write('id,content\n')
        for file in files:
            filepath = subdir + os.sep + file
            id = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
            with open(filepath, 'r') as f:
                content = f.read().strip().replace('\n', ' ').replace("\"", "'")
                out.write(id + ",\"" + content +"\"\n")

for subdir, dirs, files in os.walk(rootdir + os.sep + 'female'):
    with open(rootdir + os.sep + 'bigTxtFemale' + os.sep + 'data.csv', 'w') as out:
        out.write('id,content\n')
        for file in files:
            filepath = subdir + os.sep + file
            id = re.search("^([0-9]+)[a-zA-Z]_*[0-9]*-", file).group(1)
            with open(filepath, 'r') as f:
                content = f.read().strip().replace('\n', ' ').replace("\"", "'")
                out.write(id + ",\"" + content +"\"\n")