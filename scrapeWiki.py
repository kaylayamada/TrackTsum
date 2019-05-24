# import libraries
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url = 'https://disneytsumtsum.fandom.com/wiki/MyTsum_Chart'

# query the website and return the html to the variable 'page'
page = urlopen(url)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'lxml')
#print(soup.get_text()) #checks that soup works

# take out the <div> of the data
table = soup.find("table", {"class":"article-table"})
tsums = []

class tsum:
    name = "N/A"
    imageurl = "N/A"
    series = "N/A"
    numToCharge = 0
    description = "N/A"
    categories = []
    def __init__(self, name, imageurl, series, numToCharge, description):
        self.name = name
        self.imageurl = imageurl
        self.series = series
        self.numToCharge = numToCharge
        self.description = description



for row in table.find_all('tr'):
    details = row.find_all("a")
    if len(details)>0:
        titleName = details[1].get('title')
        imageurl = details[0].get('href')
        series = details[2].text
        columns = row.find_all('td')
        numToCharge = columns[4].text
        description = columns[6].text
        tsums.append(tsum(titleName, imageurl, series, numToCharge, description))
        #tsums.append([titleName, image, series, numToCharge, description])

#for tsum in tsums:
#    print(tsum.name)
#    print(tsum.imageurl)
#    print(tsum.series)
#    print(tsum.numToCharge)
#    print(description)
#    print('-------------------')
