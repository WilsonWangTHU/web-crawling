from urllib2 import urlopen
from bs4 import BeautifulSoup

# try to use the class of bs object
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# the table tag in the html is a "table". The "tr" tag, which is
# the child, is the row of the table
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)  # the children are the contents of the first row

for siblings in \
        bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(siblings)  # the children are the contents of the first row

# the price of a given image
price = bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).\
    parent.previous_sibling
print(price.get_text())
