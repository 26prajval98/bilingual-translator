from bs4 import BeautifulSoup
import copy
import re


def get_sentences(fname):
    content = open(fname, "r", encoding="utf-8").read()
    content = re.sub(r"<fs.*>", "<fs/>", content)

    sp = BeautifulSoup(content, "html.parser")

    [sss.extract() for sss in sp("fs")]

    sentences = []

    for ss in sp.find_all("sentence"):
        x = "".join(ss.findAll(text=True))
        x = re.sub(r"\t", "", x)
        x = re.sub(r"[A-Za-z]|_|\)\)\n|\(\(|[0-9]+\.[0-9]+", "", x)
        x = re.split(r"[0-9]+\n", x)

        for i in range(len(x)):
            x[i] = re.sub(r"[0-9]", "", x[i])
            x[i] = re.split("\n", x[i])[0:-1]

        temp_sentences = [""]
        for i in range(len(x)):
            t = x[i]
            if len(t) == 0:
                t = [""]
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
        # print(temp_sentences)
        sentences = [*sentences, *temp_sentences]

    return sentences


data_sets = 16
sets = [i+1 for i in range(data_sets)]

f = open("dataset.txt", "a+", encoding="utf-8")

for i in sets:
    s = get_sentences("data (" + str(i) + ").txt")
    print(i)
    txt = '\n'.join(s)
    f.write(txt)
