import requests
from bs4 import BeautifulSoup
import pprint

pn, urlpn = 1, ''
dict_Results, li_scores, FnResult1 = {}, [], []
xsoup = BeautifulSoup()
all_scores = xsoup()
all_links = xsoup()


#    print(type(resp))
#    print(type(xsoup))
#   print(type(all_links), '\n')

def readylinks():
    all_links = xsoup.select('.titleline')
    return all_links


def readyscores():
    all_scores = xsoup.select('.score')
    return all_scores


def articleofhighpoints(links, score):
    FnResult, xpoint = [], 0
    for idx, link in enumerate(links):
        xpoint = int(score[idx].getText().replace(' points', ''))
        if xpoint >= 100:
            print(idx, xpoint)
            #            li_scores.append(score[idx].getText().strip(' points'))
            #            dict_Results.update({links[idx].text: links[idx].find('a').get('href')})
            FnResult.append({"Title is ": link.text, "URL is ": link.find('a').get('href'), "with Points ": xpoint})
    return FnResult


while pn < 5:
    urlpn = 'https://news.ycombinator.com/news?p=' + str(pn)
    print(urlpn)
    resp = requests.get(urlpn)
    xsoup = BeautifulSoup(resp.text, 'html.parser')
    all_scores = readyscores()
    all_links = readylinks()
    FnResult1 += articleofhighpoints(links=all_links, score=all_scores)
    print('page',pn,len(FnResult1))
    pn += 1

#pprint.pprint(FnResult1)

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
