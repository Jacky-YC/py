from urllib import request
from urllib.request import Request

from bs4 import BeautifulSoup

import mail

dict = {}
url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


def get_html(url):
    req = Request(url, headers=headers)
    html = request.urlopen(req).read().decode()
    return html


def parse_html(htmlfile):
    bs = BeautifulSoup(htmlfile, 'html.parser')
    movie_zone = bs.find('ol')
    movie_list = movie_zone.find_all('li')
    for movie in movie_list:
        dict.__setitem__(movie.find('span', attrs={'class': 'title'}).getText(),
                         movie.find('span', attrs={'class': 'inq'}).getText())


def to_content(**kwargs):
    message = ''
    n = 1
    for k, v in kwargs.items():
        message += 'top %s 名称: <%s> 简介: %s \n' % (n, k, v)
        n += 1
    return message


def get_receivers():
    try:
        file = open('mail.txt', 'r')
        return file.readlines()
    finally:
        if file:
            file.close()


def send_top25_movies():
    parse_html(get_html(url))
    mail.send_mail(get_receivers(), title='top25 电影', subject=to_content(**dict))

if __name__ == '__main__':
    send_top25_movies()
