import requests
from bs4 import BeautifulSoup

resp = requests.get('https://news.ycombinator.com/news')
print(type(resp))

xsoup = BeautifulSoup(resp.text, 'html.parser')
print(type(xsoup))

# print(xsoup.find_all('a'))
all_Spans = xsoup.find_all('span', class_='score')
all_Spans_alt = xsoup.select('a')
print(all_Spans_alt)

li_len = len(all_Spans)
scores, i = [], 0
while i < li_len:
    scores.append(all_Spans[i].text)
    #print(type(scores[i]))
    i += 1
# scores = all_As
print(scores[0])


def scoremorethan100():
    #    for score in all_Spans:
    return
