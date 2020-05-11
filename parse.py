import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


def parse_last_news(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    news_list = soup.find('a', 'link_nodecor link_colored-hover')
    title = news_list.text
    title = title.replace('\n', '').replace('  ', '')
    link = news_list.get('href')
    return {'title': title, 'link': link}
