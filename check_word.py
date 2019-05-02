import io
import numpy as np
from scipy import spatial


def load_data(fin, no):
	x = {}
	i = 0
	for line in fin:
		tokens = line.rstrip().split(' ')
		x[tokens[0]] = tokens[1:]
		i += 1
		if i > no:
			break
	return x


def return_t_list(sentence, data):
	t_list = {x: np.array([]) for x in sentence.split(" ")}
	for x in t_list:
		t_list[x] = data.get(x, None)


	return t_list


def cbow(sentence, words):
	fin = io.open("data.vec", 'r', encoding='utf-8', newline='\n', errors='ignore')
	n, d = map(int, fin.readline().split())

	data = load_data(fin, 100000)

	t_list_sentence = return_t_list(sentence, data)
	x = np.zeros((300, ), dtype=np.float64)
	t = 0
	for i in t_list_sentence:
		if t_list_sentence[i] is not None:
			x = x + np.array(t_list_sentence[i], dtype=np.float64)
			t += 1

	x /= t

	words_list = [[], []]
	t_list_words = return_t_list(" ".join(words), data)

	for i in t_list_words:
		if t_list_words[i] is not None:
			words_list[0].append(i)
			words_list[1].append(np.array(t_list_words[i], dtype=np.float64))

	A = spatial.KDTree(words_list[1])

	print(words_list[0][A.query(x)[1]])


cbow("ಈ ಹಿಡಿಯೋಕೆ ಮಾಡಬೇಕು", ['ನಿವ್ವಳ', 'ಜಾಲ', 'ಬಲೆ', 'ಕಲ್ಲಿ', 'ಐನು', 'ಕಳೆತವಿಲ್ಲದ', 'ಸಂಪಾದಿಸು', 'ಲಾಭಗಳಿಸು'])