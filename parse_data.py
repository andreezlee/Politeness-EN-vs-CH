import csv
from nltk.tokenize import word_tokenize

# Creating bigrams and unigrams from the data
with open('RatingData - Sheet1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    unigrams = {}
    bigrams = {}
    next(csv_reader, None)
    for row in csv_reader:
        msg = word_tokenize(row[1].lower())
        msg = ['<s>' if x=='.' or x=='!' or x=='?' else x for x in msg]
        for i in range(len(msg)):
            if msg[i] not in unigrams:
                unigrams[msg[i]] = [0,0,0]
            bigram = '<s>_'+msg[i] if i == 0 else msg[i-1]+'_'+msg[i]
            if bigram not in bigrams:
                bigrams[bigram] = [0,0,0]

            unigrams[msg[i]][0] += float(row[4])
            bigrams[bigram][0] += float(row[4])
            unigrams[msg[i]][1] += float(row[8])
            bigrams[bigram][1] += float(row[8])
            unigrams[msg[i]][2] += 1
            bigrams[bigram][2] += 1

    for i in unigrams.keys():
        s = unigrams[i]
        unigrams[i] = [s[0]/s[2],s[1]/s[2]]
    for i in bigrams.keys():
        s = bigrams[i]
        bigrams[i] = [s[0]/s[2],s[1]/s[2]]

    print("unigrams")
    for i in unigrams.keys():
        s = unigrams[i]
        if abs(s[0] - s[1]) >= 1.5:
            print(i + ": " + str(s[0]) + " " + str(s[1]))
    print("bigrams")
    for i in bigrams.keys():
        s = bigrams[i]
        if abs(s[0] - s[1]) >= 1.5:
            print(i + ": " + str(s[0]) + " " + str(s[1]))

