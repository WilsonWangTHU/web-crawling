from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup


def getTitle(web):
    try:
        html = urlopen(web)
    except HTTPError as e:
        print('A HTTP error occured as {}'.format(e))
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.h2
    except AttributeError as e:
        print('An AttributeError occured as {}'.format(e))
        return None
    return title

title = getTitle(
    "http://www.pythonscraping.com/exercises/exercise1.html")
print(title)
