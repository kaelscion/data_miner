from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

ingredients = []

def get_recipe_data(links):
        #for link in link_data:
            html=urlopen(links).read()
            soup=BeautifulSoup(html,"lxml")
            recipe_title=soup.h1.get_text()
            get_recipe_ingredients=soup.find('p', attrs={'style':'margin-left: 40px;'})
            with open("C:/users/Jake/Desktop/contents.csv", 'w') as csvfile:
                content_header=['Title', 'Ingredients']
                writer=csv.DictWriter(csvfile, fieldnames=content_header)
                writer.writeheader()
                ingredient_list=get_recipe_ingredients.get_text()
                writer.writerow({'Title':recipe_title.encode('utf-8').strip(), 'Ingredients':ingredient_list.encode('utf-8').strip()})

get_recipe_data("http://greatist.com/health/twice-baked-broccoli-and-kale-stuffed-potatoes")