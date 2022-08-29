import requests
from bs4 import BeautifulSoup
import json

limit = '30'
last_dt = '2022-07-04%2007:57:33.933739'

url = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={last_dt}'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
data = json.loads(response.text)
data = data['data']

with open('my.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('my.json', 'r') as file:
   file = json.load(file)
