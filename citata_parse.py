import requests
from bs4 import BeautifulSoup


# получаем имя автора, их цитаты и теги
def get_data():
    for content in range(1, 11):
        url = "https://example.com/"
        responce = requests.get(url)
        soup = BeautifulSoup(responce)
        data = soup.find_all("some_tags")
        for item in data:
            name = item.find("some_tags")
            text = item.find("some_tags")
            tags = item.find("some_tags")
            yield name, text, tags
