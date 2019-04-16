# https://www.shabdkosh.com/search-dictionary?e=dog&lc=kn&sl=en&tl=kn

from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_kannada_word(search_word):

	dict_page = 'https://www.shabdkosh.com/search-dictionary?e=' + search_word + '&lc=kn&sl=en&tl=kn'

	page = urlopen(dict_page)

	soup = BeautifulSoup(page, 'html.parser')

	res_list = soup.find('ol', attrs={'class':'eirol'})

	res = res_list.text

	print(res)


search_word = "bank"

get_kannada_word(search_word)

