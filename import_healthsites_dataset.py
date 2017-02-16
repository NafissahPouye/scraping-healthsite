import requests r
from bs4 import BeautifulSoup as Soup
import time

def dataset():
scrape_url = 'https://healthsites.io/api/v1/healthsites/facilities?page=1&format=json'
q = r.get(scrape_url)
s = Soup(q.text)
filenamestart = 'Healthsites'
return dataset

