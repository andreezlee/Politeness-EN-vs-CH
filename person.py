
# Exploring first vs second vs third person
all_pnouns = set(['i','me','myself','my','mine','we','us','our','ourselves',
    'ours','you','yourself','your','yours', 'yourselves','he','she','it','him',
    'her','his','hers','its','himself','herself','itself','they','them',
    'themselves','their','theirs'])

pnouns = {}
pnouns['1sg'] = set(['i','me','myself','my','mine'])
pnouns['1pl'] = set(['we','us','our','ourselves','ours'])
pnouns['2sg'] = set(['you','yourself','your','yours'])
pnouns['2pl'] = set(['yourselves'])
pnouns['3sg'] = set(['he','she','it','him','her','his','hers','its','himself','herself','itself'])
pnouns['3pl'] = set(['they','them','themselves','their','theirs'])

class PronounCounter:

    def __init__(self, is_pos, is_native):
        self.is_pos = is_pos
        self.is_native = is_native
        self.counts = {}
        self.counts['1sg'] = 0
        self.counts['1pl'] = 0
        self.counts['2sg'] = 0
        self.counts['2pl'] = 0
        self.counts['3sg'] = 0
        self.counts['3pl'] = 0
        self.total = 0

    def finalize(self):
        if self.total != 0:
            for i in self.counts:
                self.counts[i] = self.counts[i]/self.total
        return self.counts

    def add(self, token, is_pos, is_native):
        if is_pos == self.is_pos and is_native == self.is_native and token in all_pnouns:
            for i in pnouns:
                if token in pnouns[i]:
                    self.counts[i] += 1
                    self.total += 1
                    break

p_nn_counts = PronounCounter(True, False)
p_n_counts = PronounCounter(True, True)
n_nn_counts = PronounCounter(False, False)
n_n_counts = PronounCounter(False, True)
all_counters = [p_nn_counts, p_n_counts, n_nn_counts, n_n_counts]


import csv
from nltk.tokenize import word_tokenize

with open('RatingData - Sheet1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, None)
    for row in csv_reader:

        native_score = float(row[4])
        pos = native_score > 0
        non_native_score = float(row[8])
        nn_pos = non_native_score > 0
        

        msg = word_tokenize(row[1].lower())
        for i in msg:
            for j in all_counters:
                j.add(i,pos if j.is_native else nn_pos,True)
                j.add(i,pos if j.is_native else nn_pos,False)
for j in all_counters:
    j.finalize()
    print("Model: " + ("positive" if j.is_pos else "negative") + " ratings by " + 
        ("native" if j.is_native else "non-native") + " speakers")
    print(j.counts)

# Outcome: no differences between native and non-native speakers.