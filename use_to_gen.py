from bs4 import BeautifulSoup
import copy
import re

content = open("source.txt", "r", encoding="utf-8").read()
content = re.sub(r"<fs.*>", "<fs/>", content)

sp = BeautifulSoup(content, "html.parser")

[s.extract() for s in sp("fs")]

sentences = []

for s in sp.find_all("sentence"):
    x = "".join(s.findAll(text=True))
    x = re.sub(r"\t", "", x)
    x = re.sub(r"[A-Za-z]|_|\)\)\n|\(\(|[0-9]+\.[0-9]+", "", x)
    x = re.split(r"[0-9]+\n", x)
    for i in range(len(x)):
        x[i] = re.split("\n", x[i])[0:-1]

    temp_sentences = [""]
    for i in range(len(x)):
        t = x[i]
        if t[0] == ".":
            break
        temp_sentences2 = copy.deepcopy(temp_sentences)
        temp_sentences = []
        for j in range(len(t)):
            new_word = t[j]
            for k in range(len(temp_sentences2)):
                if new_word != "":
                    ns = temp_sentences2[k] + new_word + " "
                else:
                    ns = temp_sentences2[k]
                temp_sentences.append(ns)
    sentences = [*sentences, *temp_sentences]
