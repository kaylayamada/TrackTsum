# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://disneytsumtsum.fandom.com/wiki/MyTsum_Chart'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

