from urllib2 import urlopen
from bs4 import BeautifulSoup
from bs4 import re
pages = set()


def getLinks(pageUrl):
    global pages  # make sure the global name is used
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    # testing the structure of the pages
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("Cannot find the main text or edit page")

    for links in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in links.attrs:
            if links.attrs['href'] not in pages:
                newPage = links.attrs['href']
                pages.add(newPage)
                print(newPage)
                getLinks(newPage)
        else:
            print('How is it possible?')
            print(links)
            print('How is it possible?')

getLinks('')
