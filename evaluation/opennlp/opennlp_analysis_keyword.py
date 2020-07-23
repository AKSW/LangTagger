import os
from sklearn import metrics

import pandas as pd

result = []


def extractLan(f):
    global result
    count = 0
    while count < 1458:
        line = f.readline()
        if line == "\n":
            continue
        result.append(line[:3])
        count += 1


with open('../key_word_output.txt', 'r') as f:
    extractLan(f)

# English, Spanish, German, Italian, French, Dutch, Romanian
# {'en': 0, 'de': 1, 'es': 2, 'it': 3, 'fr': 4, 'nl': 5, 'ro': 6}


label = {'eng': 0, "spa": 2, "deu": 1, "ita": 3, "fra": 4, "nld": 5, "ron": 6, "other": 7}

for i in range(len(result)):
    key = result[i]
    if key in label:
        result[i] = label[key]
    else:
        result[i] = 7

# print(result.count(7))

df = pd.read_csv("../keyword.csv")
columns = ['pt_BR', 'hi_IN', 'fa']

for col in columns:
    df = df[df.lang != col]

possible_labels = df["lang"].unique()

label_dict = {}
for index, possible_label in enumerate(possible_labels):
    label_dict[possible_label] = index

df['lang'] = df.lang.replace(label_dict)

y_true = list(df['lang'])

tot = len(result)
correct = 0
for i in range(tot):
    if result[i] == y_true[i]:
        correct += 1

score = correct / tot

print(f"score: {score}")
