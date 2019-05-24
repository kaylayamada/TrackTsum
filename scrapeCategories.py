#import pprint
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
tsums = {}
tsumNames = []

class tsum:
    def __init__(self, name, imageurl, series, numToCharge, description):
        self.name = name
        self.imageurl = imageurl
        self.series = series
        self.numToCharge = numToCharge
        self.description = description
        self.categories = []
    def addCategory(self, string):
        self.categories.append(string)

def tsumExists(tsumName):
    return tsumName in tsumNames


for row in table.find_all('tr'):
    details = row.find_all("a")
    if len(details)>0:
        tsumName = details[1].text
        if "Musketeer" in tsumName:
            tsumName = "Musketeer "+tsumName[17:]
        elif "Panchito" in tsumName:
            tsumName = "Panchito Pistoles"
        elif "Jamba" in tsumName:
            tsumName = "Dr. Jumba Jookiba"
        elif "Frankenstein" in tsumName:
            tsumName = "Bolt-head Goofy"
        elif "Boogie" in tsumName:
            tsumName = "Oogie Boogie"
        elif "Santa Jack" in tsumName:
            tsumName = "Holiday Jack"
        imageurl = details[0].get('href')
        series = details[2].text
        columns = row.find_all('td')
        numToCharge = columns[4].text
        description = columns[6].text
        #tsums.append(tsum(titleName, imageurl, series, numToCharge, description))
        tsums[tsumName] = tsum(tsumName, imageurl, series, numToCharge, description)


#for tsum in tsums:
#    tsumNames.append(tsum.name)
tsumNames = list(tsums)


# Get links to category attributes
atturl = 'https://disneytsumtsum.fandom.com/wiki/Category:Attributes'
page = urlopen(atturl)
soup = BeautifulSoup(page, 'lxml')
list = soup.find("div", {"class":"category-page__members"})
pages = list.find_all("a")
links = ["https://disneytsumtsum.fandom.com"+page.get('href') for page in pages]

# Label tsum tsum categories with attributes
for link in links:
    page = urlopen(link)
    soup = BeautifulSoup(page, 'lxml')
    title = soup.find('h1', {"class":"page-header__title"})
    CategoryTitle = title.text
    #print(CategoryTitle)
    if ( CategoryTitle != "Color Families")and( CategoryTitle != "Colors")and\
        (CategoryTitle != "Gender")and(CategoryTitle != "Initials")and\
        (CategoryTitle != "Pointy Hair")and(CategoryTitle!="Series")and\
        (CategoryTitle!= "Skills")and(CategoryTitle != "Springy hair")and\
        (CategoryTitle!= "Premium"):
        list = soup.find("ul", {"class":"category-page__trending-pages"})
        names = list.find_all("figcaption")
        CategoryNames = [name.text for name in names] #Tsum tsum in that Category
        # check if exists as tsum tsums
        for tsumName in CategoryNames:
            if tsumName in tsums:
                tempTsum = tsums[tsumName]
                tempTsum.categories.append(CategoryTitle)
            else:
                raise Exception("Tsum tsum not in database: "+tsumName)
        #print(CategoryTitle)
        #print(CategoryNames)
        #print(count == len(CategoryNames))

#SKILLS
skillurl = 'https://disneytsumtsum.fandom.com/wiki/Category:Skills'
page = urlopen(skillurl)
soup = BeautifulSoup(page, 'lxml')
list = soup.find("div", {"class":"category-page__members"})
pages = list.find_all("a")
skillLinks = ["https://disneytsumtsum.fandom.com"+page.get('href') for page in pages]
for link in skillLinks:
    page = urlopen(link)
    soup = BeautifulSoup(page, 'lxml')
    title = soup.find('h1', {"class":"page-header__title"})
    CategoryTitle = title.text
    list = soup.find("ul", {"class":"category-page__trending-pages"})
    names = list.find_all("figcaption")
    CategoryNames = [name.text for name in names] #Tsum tsum in that Category
    # check if exists as tsum tsums
    for tsumName in CategoryNames:
        if tsumName in tsums:
            tempTsum = tsums[tsumName]
            tempTsum.categories.append(CategoryTitle)
        else:
            raise Exception("Tsum tsum not in database: "+tsumName)


for tsum in tsums:
    print(tsums[tsum].name)
    #print(tsums[tsum].imageurl)
    #print(tsums[tsum].series)
    #print(tsums[tsum].description)
    print(tsums[tsum].categories)
    print('-------------------')
