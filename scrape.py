import requests
from bs4 import BeautifulSoup

resp = requests.get('https://news.ycombinator.com/news')
print(type(resp))

xsoup = BeautifulSoup(resp.text, 'html.parser')
print(type(xsoup))

all_scores = xsoup.select('.score')
all_links = xsoup.select('.titleline')
print(type(all_links),'\n')

dict_Results = {}

def GEtNAmesLInks():
    li_len = len(all_links)
    result, i = [], 0
    while i < li_len:
        dict_Results.update({all_links[i].text:all_links[i].find('a').get('href')})
        i += 1
    return


def GEtSCores():
    # greater than 100 score points in a list
    li_len = len(all_scores)
    scores, i = [], 0
    while i < li_len:
        scores.append(all_scores[i].text)
        # print(scores[i])
        i += 1
    return


GEtSCores()
GEtNAmesLInks()

print(dict_Results[2])