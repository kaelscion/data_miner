from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

class data_miner:

    recipe_links = []

    def __init__(self, base_url, output_file):
       self.base_url = base_url
       self.output_file = output_file

    def get_link_data(self):
        #load_url_and_soup()
        html=urlopen(self.base_url).read()
        soup=BeautifulSoup(html,"lxml")
        get_raw_links=soup.find('div', 'article-body-content')
        self.recipe_links=[h4.a["href"]for h4 in get_raw_links.findAll('h4')]

    def write_out(self):
        with open(self.output_file, 'w') as csvfile:
            field_names = ['Recipe Link']
            writer=csv.DictWriter(csvfile, fieldnames=field_names,)
            writer.writeheader()
            for item in self.recipe_links:
                writer.writerow({'Recipe Link':str(item)})

    def run_scraper(self):
        self.get_link_data()
        self.write_out()

x = data_miner("http://greatist.com/health/cheap-healthy-lunch-dinner-entree-recipes", "C:/Users/Jake/Desktop/test_data.csv")
x.run_scraper()
#x.get_recipe_data("http://sweetpotatochronicles.com/2014/01/vitamin-week-salmon-parcels/")

