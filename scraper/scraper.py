import requests
from bs4 import BeautifulSoup


def get_article(url, set_links, arr_links, i):
    wiki_page = requests.get(url)
    sp = BeautifulSoup(wiki_page.content, 'lxml')
    article_text = ''

    art = sp.find_all("p")

    links = sp.find_all("a", href=True)

    i += 1

    for element in art:
        article_text += ''.join(element.findAll(text=True))

    for l in links:
        link = l['href']
        if isinstance(link, str) and link.startswith("/wiki") and link not in set_links:
            set_links.add(link)
            arr_links.append(link)

    return i, set_links, arr_links, article_text


No_ARTICLES = 100

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

    print(arr_urls)

    if itr > No_ARTICLES or itr >= len(arr_urls):
        break

f.close()
