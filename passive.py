import spacy
from spacy.matcher import Matcher
import csv

# Model for matching passive voice
nlp = spacy.load('en_core_web_lg')
matcher = Matcher(nlp.vocab)
passive_rule = [{'DEP':'nsubjpass'},{'DEP':'aux','OP':'*'},{'DEP':'auxpass'},{'TAG':'VBN'}]
matcher.add('Passive',None,passive_rule)

p_n = [0,0]
p_nn = [0,0]
n_n = [0,0]
n_nn = [0,0]

with open('RatingData - Sheet1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader, None)
    for row in csv_reader:

        native_score = float(row[4])
        pos = native_score > 0
        non_native_score = float(row[8])
        nn_pos = non_native_score > 0

        # Passive given fits category
        """if pos:
            p_n[1] += 1
        else:
            n_n[1] += 1
        if nn_pos:
            p_nn[1] += 1
        else:
            n_nn[1] += 1

        text = row[1]
        doc = nlp(text)
        matches = matcher(doc)
        if len(matches) > 0:
            if pos:
                p_n[0] += 1
            else:
                n_n[0] += 1
            if nn_pos:
                p_nn[0] += 1
            else:
                n_nn[0] += 1"""

        # Fits category given passive
        text = row[1]
        doc = nlp(text)
        matches = matcher(doc)
        if len(matches) > 0:
            if pos:
                p_n[0] += 1
            else:
                n_n[0] += 1
            if nn_pos:
                p_nn[0] += 1
            else:
                n_nn[0] += 1
            p_n[1] += 1
            n_n[1] += 1
            p_nn[1] += 1
            n_nn[1] += 1
print("Model: positive ratings by native speakers")
print(p_n[0]/p_n[1])
print("Model: negative ratings by native speakers")
print(n_n[0]/n_n[1])
print("Model: positive ratings by non-native speakers")
print(p_nn[0]/p_nn[1])
print("Model: negative ratings by non-native speakers")
print(n_nn[0]/n_nn[1])