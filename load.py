import io
import numpy as np

fin = io.open("data.vec", 'r', encoding='utf-8', newline='\n', errors='ignore')
n, d = map(int, fin.readline().split())
sentence = "ನನ್ನ ಹೆಸರು ಅಖಿಲ್"
tList = {x: {"p": 0, "data": np.array([])} for x in sentence.split(" ")}
for line in fin:
    tokens = line.rstrip().split(' ')
    if tokens[0] in tList.keys():
        tList[tokens[0]]["p"] = 1
        tList[tokens[0]]["data"] = tokens[1:]

    done = True
    for x in tList.keys():
        if tList[x]["p"] == 0:
            done = False

    if done:
        break
