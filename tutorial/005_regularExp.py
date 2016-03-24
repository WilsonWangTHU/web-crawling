from urllib2 import urlopen
from bs4 import BeautifulSoup
from bs4 import re

# try to use the class of bs object
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

for iImage in images:
    print(iImage)

print(bsObj.findAll(lambda tag: len(tag.attrs) == 2))
