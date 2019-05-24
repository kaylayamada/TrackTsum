#import scrapeWiki.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://disneytsumtsum.fandom.com/wiki/Category:Beaked'
page = urlopen(url)
soup = BeautifulSoup(page, 'lxml')
list = soup.find("ul", {"class":"category-page__trending-pages"})
names = list.find_all("figcaption")
beakNames = [name.text for name in names]
