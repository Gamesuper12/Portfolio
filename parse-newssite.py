import requests
from bs4 import BeautifulSoup
from time import sleep

#Получаем ссылки:
def get_url():
    url = 'https://example.com/'
    responce = requests.get(url)
    for item in data:
        url_card = 'find urls'
        for cards in url_card:
            yield urls

#Собираем данные в ссылках
def get_data():
    for info in get_url():
        responce = requests.get(info)    
        yield info
