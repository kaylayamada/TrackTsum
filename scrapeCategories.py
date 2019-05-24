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
        titleName = details[1].text
        imageurl = details[0].get('href')
        series = details[2].text
        columns = row.find_all('td')
        numToCharge = columns[4].text
        description = columns[6].text
        #tsums.append(tsum(titleName, imageurl, series, numToCharge, description))
        tsums[titleName] = tsum(titleName, imageurl, series, numToCharge, description)

# Tsum tsums missed
tsums["Dr. Jumba Jookiba"] = tsum("Dr. Jumba Jookiba", "https://vignette.wikia.nocookie.net/disneytsumtsum/images/8/84/Dr.Jamba.png/revision/latest?cb=20180901000816",\
    "Lilo & Stitch", 16, "Clears a zig-zag of Tsums!")

#for tsum in tsums:
#    tsumNames.append(tsum.name)
tsumNames = list(tsums)
#print(tsumNames)



# Get links to category attributes
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://disneytsumtsum.fandom.com/wiki/Category:Attributes'
page = urlopen(url)
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
        count = 0
        #TODO: Make dictionary of tsumtsum names from a better list

        for tsumName in CategoryNames:
            if tsumName in tsums:
                tempTsum = tsums[tsumName]
                tempTsum.categories.append(CategoryTitle)
                count = count + 1
            elif "Musketeer" in tsumName:
                tsums["Three Musketeers "+tsumName[10:]].categories.append(CategoryTitle)
                count = count + 1
            elif "Panchito" in tsumName:
                tsums["Panchito"].categories.append(CategoryTitle)
                count = count + 1
            elif "Bolt" in tsumName:
                tsums["Frankenstein Goofy"].categories.append(CategoryTitle)
                count = count + 1
            elif "Boogie" in tsumName:
                tsums["Boogie"].categories.append(CategoryTitle)
                count = count + 1
            else:
                raise Exception("Tsum tsum not in database: "+tsumName)
        #print(CategoryTitle)
        #print(CategoryNames)
        #print(count == len(CategoryNames))

for tsum in tsums:
    print(tsums[tsum].name)
    #print(tsums[tsum].imageurl)
    #print(tsums[tsum].series)
    #print(tsums[tsum].description)
    print(tsums[tsum].categories)
    print('-------------------')
