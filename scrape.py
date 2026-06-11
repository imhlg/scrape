import requests
from bs4 import BeautifulSoup
import pprint

resp = requests.get('https://news.ycombinator.com/news')
print(type(resp))

xsoup = BeautifulSoup(resp.text, 'html.parser')
print(type(xsoup))

all_scores = xsoup.select('.score')
all_links = xsoup.select('.titleline')
print(type(all_links), '\n')

dict_Results, li_scores, FnResult1 = {}, [], []


def articleofhighpoints(links, score):
    FnResult, xpoint = [], 0
    for idx, link in enumerate(links):
        xpoint = int(score[idx].getText().replace(' points', ''))
        if xpoint >= 100:
            #            li_scores.append(score[idx].getText().strip(' points'))
            #            dict_Results.update({links[idx].text: links[idx].find('a').get('href')})
            FnResult.append({"Title is ": link.text, "URL is ": link.find('a').get('href'), "with Points ": xpoint})
    return FnResult


FnResult1 = articleofhighpoints(all_links, all_scores)

pprint.pprint(FnResult1)

'''print(FnResult)

def GEtSCores():
    # greater than 100 score points in a list
    li_len = len(all_scores)
    scores, i = [], 0
    while i < li_len:
        scores.append(all_scores[i].text)
        # print(scores[i])
        i += 1
    return

GEtSCores()'''
