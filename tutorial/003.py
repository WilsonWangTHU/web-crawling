from urllib2 import urlopen
from bs4 import BeautifulSoup

# try to use the class of bs object

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

if 'bookReader' not in locals():
    bookReader = BeautifulSoup(html, 'lxml')

nameList = bookReader.findAll("span", {"class", "green"})


"""
for sentence in nameList:
    print(sentence)  # the sentence is a bs element.tag
    print(sentence.get_text())  # it is the actual text of the object
    """
numPrince = bookReader.findAll(text='the prince')
print(numPrince)
