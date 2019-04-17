from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from nltk.corpus import words
import json
import os
from collections import defaultdict


def get_kannada_word(search_word):
	vals = []
	dict_page = 'https://www.shabdkosh.com/search-dictionary?e='+search_word+'&lc=kn&sl=en&tl=kn'

	req = Request(dict_page, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req)

	soup = BeautifulSoup(page, 'html.parser')
	res_list = soup.find_all('ol', {'class': 'eirol'})

	for ol in res_list:
		li = ol.find_all('li')
		for a in li:
			for x in a.find_all('a'):
				t = x.text
				if len(t.split(' ')) <= 1:
					vals.append(t)
	return vals


def return_english(sentence):
	for i in range(len(sentence)):
		if sentence[i] in words.words():
			return i, sentence[i]

	return -1, None


def calculate_prob(t_a, m):
	t = [None, None]
	prob = 1
	for ww in t_a:
		prob_t = m[tuple(t)].get(ww, None)
		if prob_t is None:
			prob *= 10 ** -10
		t.append(ww)
	return prob


def get_sentence(sentence, model):
	sentence_array = sentence.split(" ")

	idx, word = return_english(sentence_array)

	if idx != -1:
		wws = get_kannada_word(word)
		p = - 100
		chosen_word = ""
		t_array = sentence_array[:]
		for w in wws:
			t_array[idx] = w
			t = calculate_prob(t_array, model)
			if t > p:
				p = t
				chosen_word = w

		t_array[idx] = chosen_word
		print("New sentence : ", t_array)
		return t_array


def load_json(path, file):
	os.chdir(path)
	b = defaultdict(lambda: defaultdict(lambda: 0.2))
	if os.path.isfile(file):
		f = open(file, "r", encoding="utf-8")

		json_data = json.loads(f.read())

		b = defaultdict(lambda: defaultdict(lambda: 0.2))

		for t in json_data:
			string = t[:]
			t1, t2 = string.split(":", 1)
			if t1 == "None":
				t1 = None
			if t2 == "None":
				t2 = None
			b[(t1, t2)] = json_data[string]

	return b


if __name__ == "__main__":
	sw = "name"
	print(get_kannada_word(sw))
