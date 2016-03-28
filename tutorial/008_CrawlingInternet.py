from urllib2 import urlopen
from bs4 import BeautifulSoup
from bs4 import re
import datetime
import random

pages = set()


def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for links in bsObj.find("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if links.attrs['href'] is not None:
            if links.attrs['href'] not in internalLinks:
                internalLinks.append(links.attrs['href'])
    return internalLinks


def getExternalLinks(bsObj, includeUrl):
    externalLinks = []
    for links in bsObj.find("a", href=re.compile("^(www|http)((?!" + includeUrl + ").)*$")):
        if links.attrs['href'] is not None:
            if links.attrs['href'] not in externalLinks:
                externalLinks.append(links.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)

    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])

    if len(externalLinks) == 0:
        internalLinks = \
            getInternalLinks(bsObj, splitAddress(startingPage)[0])
        return # to do
