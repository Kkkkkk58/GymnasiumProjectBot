import requests
from bs4 import BeautifulSoup as BS

URL = 'http://gymn-1.ru/news.php'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
           'accept': '*/*' }

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='title')
    latest = items[1].get_text().encode('utf-8').strip().decode('utf-8')
    return latest

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = get_content(html.text)
    else:
        print('Error')
    return items

parse()
