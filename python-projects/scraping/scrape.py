import requests
from bs4 import BeautifulSoup
import pprint



#print(votes[0].get('id'))  #. - class | # - id



def sort_by_vote(hnlist):
    return sorted(hnlist, key= lambda k:k['vote'], reverse=True)

def create_custome_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href=links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points>=100:
                hn.append({'title' : title, 'link': href, 'vote' : points})
    return sort_by_vote(hn)

def morelinks():
    joined_links=[]
    joined_subtext=[]
    for i in range(3):
        res=requests.get('https://news.ycombinator.com/news?p='+str(i))
        soup = BeautifulSoup(res.text,'html.parser')
        links=soup.select('.storylink')
        subtext=soup.select('.subtext')
        joined_links=joined_links+links if len(joined_links) else links
        joined_subtext=joined_subtext+subtext if len(joined_links) else subtext
    return create_custome_hn(joined_links, joined_subtext)

pprint.pprint(morelinks())