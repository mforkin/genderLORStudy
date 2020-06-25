import os

rootdir = '/home/mforkin/LOR/data/all-split/male'
outfile = '/home/mforkin/LOR/data/all-split/male-cnts.csv'

words = {}
total_words = 0
i = 0

for subdir, dirs, files in os.walk(rootdir):
    if subdir is rootdir:
        for file in files:
            i = i + 1
            filepath = subdir + os.sep + file
            with open(filepath) as f:
                content = f.read().lower().replace('.', '').replace('!', '').replace('?', '').replace('\n', ' ').replace('\t', ' ').replace(',', '').split(' ')
                total_words = total_words + len(content)
                for w in content:
                    if w in words:
                        words[w] = words[w] + 1
                    else:
                        words[w] = 1

with open(outfile, 'w') as out:
    sorted_words = sorted(words.items(), key=lambda x: x[1] / i, reverse=True)
    out.write('avg words: ' + str(total_words / i) + '\n\n')
    for w in sorted_words:
        out.write(w[0] + ': ' + str(w[1]) + ', ' + str(w[1] / i) + '\n')
