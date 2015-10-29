from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://silentera.com/PSFL/data/W/WithinOurGates1920.html")
bsObj = BeautifulSoup(html)

title = bsObj.find("span",{"class":"psfl-title"}).get_text()


title = str(title) + ', '


paragraphs = bsObj.find_all('p')

print(title)

for p in paragraphs:
    if "Cast" in str(p):
        p = p.get_text()
        cast = str(p)
        cast = cast.replace("Cast: ","")
        print(cast)




