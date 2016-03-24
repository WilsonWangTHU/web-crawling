from urllib2 import urlopen
from bs4 import BeautifulSoup
from bs4 import re

# try to use the class of bs object
if 'html' not in locals():
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)


def getAllLinks(url):
    bsObj = BeautifulSoup(url)
    linkTag = bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    return linkTag
