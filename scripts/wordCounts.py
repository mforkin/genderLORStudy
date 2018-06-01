from nltk.util import skipgrams
import os

ignore_words = set([a.upper() for a in ['a', 'the', 'of', 'and', 'is', 'an', 'to', 'in', 'this', 'was', 'I', 'she', 'he', 'have', 'her', 'with', 'that', 'his', 'write', 'writing', 'at', 'as', 'be', 'do', 'm', 'for', 'hesitate', '', 'She', 'School', 'University', '-', '_', 'contact', 'student', 'waived', 'has', 'residency', 'students', 'year', 'letter', 'um', 'mm','_l', 'Medical', 'l', 'peer', 'level', 'likely', 'free', 'whom', 'please', 'program', 'during', 'him', 'room', 'application', 'any', 'if', 'me', 'mm', 'mm:', 'w', 'may', 'behalf']])

number_of_words = 2
skip_dist = 5

rootdir = '/Users/mike/resumeData'
outfile = '/Users/mike/resumeData/out/'

males = 0
females = 0
total_count = 0
female_grams = {}
male_grams = {}
total_grams = {}

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (file.endswith(".txt")):
            filepath = subdir + os.sep + file
            is_female = False
            if subdir.endswith('female'):
                females += 1 
                is_female = True 
            elif subdir.endswith('male'):
                males += 1
            total_count += 1
            print(filepath)
            with open(filepath, 'r') as f:
                content = f.read().upper().replace('.', '').replace('!', '').replace('?', '').split(" ")
                grams = skipgrams(content, number_of_words, skip_dist)
                for g in grams:
                    g_name = "_".join(g)
                    if len(ignore_words.intersection(g)) == 0 :
               	        if is_female:
                            if g_name in female_grams:
                                female_grams[g_name] = female_grams[g_name] + 1 
                            else:
                                female_grams[g_name] = 1
                        else:
                            if g_name in male_grams:
                                male_grams[g_name] = male_grams[g_name] + 1 
                            else:
                                male_grams[g_name] = 1
                        if g_name in total_grams:
                            total_grams[g_name] = total_grams[g_name] + 1
                        else:
                            total_grams[g_name] = 1

print("Females: %s" % females)
print("Males: %s" % males)
print("Total: %s" % total_count)

print("-------- grams ----------")
print("female: ")
for k in sorted(female_grams, key=female_grams.get, reverse=True)[0:20]:
    print(k + " - " + str(female_grams[k]))

print("male:")
for k in sorted(male_grams, key=male_grams.get, reverse=True)[0:20]:
    print(k + " - " + str(male_grams[k]))


print("total:")
for k in sorted(total_grams, key=total_grams.get, reverse=True)[0:20]:
    print(k + " - " + str(total_grams[k]))


