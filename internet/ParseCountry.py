
"""    
    This file is written about how to get and organize country's names from baseurl.

"""


import requests,json,csv
import pandas as pd
from bs4 import BeautifulSoup

baseUrl='https://www.travel-advisory.info/api'
url=requests.get(baseUrl)

soup=BeautifulSoup(url.content,'lxml')

data=soup.find('p')
data=json.loads(data.text)['data']
print(data.values())
countries=[[i,j['name'].replace('\xe9',''),j['advisory']['score'],j['advisory']['updated']] for i,j in zip(data.keys(),data.values())]
with open('countries.csv' ,'w') as w:
    w=csv.writer(w)
    w.writerows(countries)