import sys,requests,json
from bs4 import BeautifulSoup

countries=['JP','KR','FR','MX','IR','US','IN']
BaseUrl='https://www.travel-advisory.info/api'

url=requests.get(BaseUrl)
soup=BeautifulSoup(url.content,"lxml")

# the data you get is in .txt. You need to change it in .json
data=soup.find("p")
data=json.loads(data.text)['data']

for country in countries:
    datum=data[country]['advisory']
    print(data[country]['name'],datum['score'])