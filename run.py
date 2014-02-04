import sys
import re

with open('corpus.txt') as f:
    corpus = f.read()

pattern = re.compile(r" |:|;|,|-|\n|'|\.|\"|\'|!")
corpus = pattern.split(corpus.lower())
corpus = [x.strip() for x in corpus]
corpus = [x for x in corpus if len(x) > 1]



#names = sys.stdin.readlines()
#names.pop(0)
#names = ['Hugh ']

with open('boy-names-hard.txt') as f:
    names = f.read().split("\n")
names = [x.strip() for x in names]

print len(names)

for k, name in enumerate(names):
    name = name.strip().lower()
    #print name

    indices = [i for i, x in enumerate(corpus) if x == name]
    if len(indices) == 0:
        continue

    print indices

    male = ('he', 'his', 'him', 'himself', 'man', 'son', 'grandson', 'mr')
    female = ('she', 'hers', 'her', 'herself', 'woman', 'daughter', 'granddaughter', 'mrs')

    sum_male = 0
    sum_female = 0
    for idx in indices:
        print corpus[idx-10:idx+10]
        sum_male += sum([corpus[idx-10:idx+10].count(x) for x in male])
        sum_female += sum([corpus[idx-10:idx+10].count(x) for x in female])

    print sum_male
    print sum_female

    if sum_male < sum_female:
        #print 'Male'
    #else:
        print str(k) + ' ' + name