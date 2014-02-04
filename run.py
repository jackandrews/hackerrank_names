import sys
import re

RUN_COMPETITION = False


def load_hard_names():
    with open('boy-names-hard.txt') as f:
        names = f.read().split("\n")
        return [x.strip() for x in names]


def load_stdin_names():
    names = sys.stdin.readlines()
    names.pop(0)
    return names

#load and tokenise corpus into words of length > 1
with open('corpus.txt') as f:
    corpus = f.read()

pattern = re.compile(r" |:|;|,|-|\n|'|\.|\"|\'|!")
corpus = pattern.split(corpus.lower())
corpus = [x.strip() for x in corpus]
corpus = [x for x in corpus if len(x) > 1]

#load lists of name to classify
if RUN_COMPETITION:
    names = load_stdin_names()
else:
    names = load_hard_names()

for k, name in enumerate(names):
    name = name.strip().lower()

    indices = [i for i, x in enumerate(corpus) if x == name]
    if len(indices) == 0:
        continue

    male = ('he', 'his', 'him', 'himself', 'man', 'son', 'grandson', 'mr')
    female = ('she', 'hers', 'her', 'herself', 'woman', 'daughter', 'granddaughter', 'mrs')

    sum_male = 0
    sum_female = 0
    for idx in indices:
        sum_male += sum([corpus[idx-10:idx+10].count(x) for x in male])
        sum_female += sum([corpus[idx-10:idx+10].count(x) for x in female])

    if not RUN_COMPETITION:
        print str(k) + ' ' + name
        print corpus[idx-10:idx+10]
        print indices
        print sum_male
        print sum_female

    if sum_male > sum_female:
        print 'Male'
    else:
        print 'Female'