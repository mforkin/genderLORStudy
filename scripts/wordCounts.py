from nltk.util import skipgrams
import os

number_of_words = 2
skip_dist = 2

rootdir = '/Users/mike/resumeData'
outfile = '/Users/mike/resumeData/out/'

males = 0
females = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if subdir.endswith('female'):
            females += 1 
        elif subdir.endswith('male'):
            males += 1

print("Females: %s" % females)
print("Males: %s" % males)

