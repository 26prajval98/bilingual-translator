from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from nltk.corpus import words


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
				vals.append(x.text)
	return vals


def return_english(sentence):
	for i in range(len(sentence)):
		if sentence[i] in words.words():
			return i, sentence[i]

	return -1, None


if __name__ == "__main__":
	sw = "bank"
	print(get_kannada_word(sw))
