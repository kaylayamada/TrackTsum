#import scrapeWiki.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
tsumNames = []

url = 'https://disneytsumtsum.fandom.com/wiki/Tsum_Tsum'
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
lists = soup.find("div",{"class":"mw-content-ltr"})
lists2 = lists.find_all("ul")
for list2 in lists2:
    lists3 = list2.find_all("a")
    for list3 in lists3:
        if (list3.get('title')):
            tsumNames.append(list3.get('title'))
print(len(tsumNames))
#beakNames = [name.text for name in names]
