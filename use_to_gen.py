from bs4 import BeautifulSoup
import re

content = open("source.txt", "r", encoding="utf-8").read()
content = re.sub(r"<fs.*>", "<fs/>", content)

sp = BeautifulSoup(content, "html.parser")

[s.extract() for s in sp("fs")]

x = "".join(sp.find_all("sentence")[0].findAll(text=True))
x = re.sub(r"\t", "", x)
x = re.sub(r"[A-Za-z]|_|\)\)\n|\(\(", "", x)
print(x)
