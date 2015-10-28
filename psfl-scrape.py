from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://silentera.com/PSFL/data/W/WithinOurGates1920.html")
bsObj = BeautifulSoup(html)

title = bsObj.find("span",{"class":"psfl-title"})

cast = bsObj.find_all('td')[5]
cast = cast.find_all('p')[1]


print(title.get_text())


print(cast.text)
