from nltk.util import skipgrams
import os

number_of_words = 2
skip_dist = 2

rootdir = '/Users/mike/resumeData'
outfile = '/Users/mike/resumeData/out/'

males = 0
females = 0
female_grams = {}
male_grams = {}

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = subdir + os.sep + file
        is_female = False
        if subdir.endswith('female'):
            females += 1 
            is_female = True 
        elif subdir.endswith('male'):
            males += 1
        with open(filepath, 'r') as f:
            content = f.read().replace('.', '').replace('!', '').replace('?', '')
            grams = skipgrams(content)
            for g in grams:
                # add to appropriate map

print("Females: %s" % females)
print("Males: %s" % males)

