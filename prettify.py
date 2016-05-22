from bs4 import BeautifulSoup
from urllib2 import urlopen

def prettify(url):
    html=urlopen(url).read()
    soup=BeautifulSoup(html, 'html.parser')
    print soup.prettify()

prettify("http://allrecipes.com/recipes/84/healthy-recipes/")
