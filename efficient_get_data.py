from bs4 import BeautifulSoup
import copy
import re

def solve(s, n, o, file):
    if n == -1 :
        file.write(o + '\n') # check if '\n' is needed or not
        return 1
    
    x = 0
    for i in range(len(s[n])):
        x += solve(s, n-1,s[n][i]+o, file)

    return x

def make_sentences(fname, file):
    content = open(fname, "r", encoding="utf-8").read()
    content = re.sub(r"<fs.*>", "<fs/>", content)

    sp = BeautifulSoup(content, "html.parser")

    [sss.extract() for sss in sp("fs")]
    p = 0
    p_total = len(sp.find_all("sentence"))
    for ss in sp.find_all("sentence"):
        x = "".join(ss.findAll(text=True))
        x = re.sub(r"\t", "", x)
        x = re.sub(r"[A-Za-z]|_|\)\)\n|\(\(|[0-9]+\.[0-9]+", "", x)
        x = re.split(r"[0-9]+\n", x)

        my_list = []
        for i in range(len(x)):
            x[i] = re.sub(r"[0-9]", "", x[i])
            x[i] = re.split("\n", x[i])[0:-1]
            
            my_list.append(x[i])

        print(solve(my_list, len(my_list)-1, "", file))

    return

fname = "data (14).txt"
f = open("output.txt", "a+", encoding="utf-8")
make_sentences(fname, f)
