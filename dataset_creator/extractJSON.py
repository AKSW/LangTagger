import subprocess


def extract(dataset):
    execute = ["java", "-jar", "../jars/irbench-v0.0.1-beta.2.jar", "-questions", dataset]
    return subprocess.run(execute, capture_output=True).stdout.decode()



with open('qald-1-train.json', 'w') as f:
    data = extract("qald-1-train")
    f.write(data)


with open('qald-1-test.json', 'w') as f:
    data = extract("qald-1-test")
    f.write(data)

'''
qald-5-test-multilingual
qald-6-train-multilingual
qald-5-train-multilingual
qald-2-test
qald-7-train-multilingual
qald-8-train-multilingual
qald-6-test-multilingual
qald-9-test-multilingual
qald-4-test-multilingual
qald-1-test
DBpedia39-Entity-v1
DBpedia2015-Entity-v1
qald-7-test-multilingual
qald-1-train
qald-3-test-multilingual
qald-9-train-multilingual
QALD2-DBpedia39-Entity-v1
qald-3-train-multilingual
qald-4-train-multilingual
qald-8-test-multilingual
qald-2-train


'''