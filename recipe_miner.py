from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

ingredients = []

def get_recipe_data(links):
        #for link in link_data:
            html=urlopen(links).read()
            soup=BeautifulSoup(html,"lxml")
            recipe_title=soup.h1.get_text()
            get_recipe_ingredients=soup.findAll('p')
            with open("C:/users/Jake/Desktop/contents.csv", 'w') as csvfile:
                content_header=['Content']
                writer=csv.DictWriter(csvfile, fieldnames=content_header)
                writer.writeheader()
                for content in get_recipe_ingredients:
                    writer.writerow({'Content':str(content)})
            for ingredient in get_recipe_ingredients:
                ingredient_soup=BeautifulSoup(str(ingredient), "lxml")
                ingredients.append(ingredient_soup.get_text(strip=True))
            print recipe_title

        
get_recipe_data("http://greatist.com/health/twice-baked-broccoli-and-kale-stuffed-potatoes")