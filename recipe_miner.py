from bs4 import BeautifulSoup
from urllib2 import urlopen

ingredients = []

def get_recipe_data(link_data):
        #for link in link_data:
            html=urlopen(link_data).read()
            soup=BeautifulSoup(html,"lxml")
            #get_recipe_title=soup.find('h1', {'class': 'entry_title'})
            recipe_title=soup.h1.get_text()
            get_recipe_ingredients=soup.findAll(attrs={'class':'ingredient'})
            for ingredient in get_recipe_ingredients:
                ingredient_soup=BeautifulSoup(str(ingredient), "lxml")
                ingredients.append(ingredient_soup.get_text(strip=True))
            #recipe_ingredients=[ul.li["class"] for ul in get_recipe_ingredients]
            print recipe_title
            print ingredients

get_recipe_data("http://sweetpotatochronicles.com/2014/01/vitamin-week-salmon-parcels/")
