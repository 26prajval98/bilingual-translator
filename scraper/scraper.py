import requests
import re
from bs4 import BeautifulSoup


def remove_useless(s):
    s = re.sub("[\(\[].*?[\)\]]", "", s)
    s = re.sub("'.'[ ]*", ".", s)
    s = re.sub("\n+", ".", s)
    s = re.sub("[•?!,a-zA-Z:/\[\(\)\)]", "", s)
    s = re.sub("[.]", "\n", s)
    return s.strip()


def get_article(url, set_links, arr_links, i):
    wiki_page = requests.get(url)
    sp = BeautifulSoup(wiki_page.content, 'lxml')
    article_text = ''

    art = sp.find("div", {"id": "bodyContent"}).find_all("p")

    links = sp.find_all("a", href=True)

    i += 1

    for element in art:
        txt = ''.join(element.findAll(text=True))
        txt = remove_useless(txt)
        article_text += txt

    for l in links:
        link = l['href']
        if isinstance(link, str) and link.startswith("/wiki") and link not in set_links:
            set_links.add(link)
            arr_links.append(link)

    return i, set_links, arr_links, article_text


No_ARTICLES = 1000

base_url = "https://kn.wikipedia.org"

start = "/wiki/%E0%B2%AE%E0%B3%81%E0%B2%96%E0%B3%8D%E0%B2%AF_%E0%B2%AA%E0%B3%81%E0%B2%9F"

set_urls = {start}

arr_urls = [start]

f = open("articles.txt", "a+", encoding="utf-8")

itr = 0

while True:
    itr, set_urls, arr_urls, article = get_article(base_url + arr_urls[itr], set_urls, arr_urls, itr)
    f.write(article)

    print("Progress = %d / %d" % (itr, No_ARTICLES))

    if itr > No_ARTICLES or itr >= len(arr_urls):
        break

f.close()
