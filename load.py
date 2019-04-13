import io
import os
os.chdir(r"F:\NITK\6thsem\CG\kannada-rocks")

fin = io.open("data.vec", 'r', encoding='utf-8', newline='\n', errors='ignore')
n, d = map(int, fin.readline().split())
data = {}
for line in fin:
    tokens = line.rstrip().split(' ')
    print(u"" + tokens[0])
    data[tokens[0]] = map(float, tokens[1:])

print("Hi")