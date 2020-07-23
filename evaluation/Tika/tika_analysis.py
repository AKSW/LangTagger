import pandas as pd
import subprocess
from sklearn.metrics import accuracy_score
import time

data = pd.read_csv('../keyword.csv')

X = data['questions']
y = data['lang']


def detect(file):
    execute = ["java", "-jar", "../jars/tika-app-1.24.1.jar", "-l", file]
    return subprocess.run(execute, capture_output=True).stdout.decode()[:2]

count=0
out = []
for text in X:
    with open('../../X.txt', 'w') as f:
        f.write(text)
    if f.closed:
        out.append(detect('../../X.txt'))
    count += 1
    print(count)
    # if count==5:
    #     break

# print(out)
print(accuracy_score(y,out))