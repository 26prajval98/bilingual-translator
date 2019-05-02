from kannadautils import *

F = "data_bi.json"
model = load_json(os.getcwd(), F)

for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

with open("testing_data.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        txt = " ".join(line.split(" ")[:-1])
        if len(txt):
            up = " ".join(get_sentence(txt, model))
            print("Old : %s\nNew : %s\n" % (txt, up))
