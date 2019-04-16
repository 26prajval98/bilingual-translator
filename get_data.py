from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_kannada_word(search_word):

	dict_page = 'https://www.shabdkosh.com/search-dictionary?e=' + search_word + '&lc=kn&sl=en&tl=kn'

	page = urlopen(dict_page)

	soup = BeautifulSoup(page, 'html.parser')

	res_list = soup.find_all("div", {"id" : "ehresults"}).find_all('ol', {'class' : 'eirol'}) #.find('li').find('a')

	for ol in res_list:
		li = ol.find_all('li')
		for a in li:
			print(a.find(text=True))


	# res = res_list.text

	print(res_list)


search_word = "bank"

get_kannada_word(search_word)
