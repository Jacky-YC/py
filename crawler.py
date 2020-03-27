# 发请求

import smtplib
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup

SMTP_HOST = 'smtp.qq.com'


def get_weather():
    url = 'http://www.weather.com.cn/weather/101020100.shtml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    resp = requests.get(url, headers)
    resp.encoding = 'UTF-8'
    bs = BeautifulSoup(resp.text, 'html.parser')
    date = bs.find("h1").get_text()
    tem = bs.find(class_="tem").get_text()
    wea = bs.find(class_="wea").get_text()
    return tuple([date, tem, wea]);


def send_mail():
    sender = '1206290545@qq.com'
    auth_code = 'HMQOLFFYGHZDZLUW'
    receivers = ['1206290545@qq.com', 'jacky.ye@fastonetech.com']
    weather = get_weather()
    message = r'日期: %s 温度: %s 天气: %s' % (weather[0], weather[1], weather[2])

    msg = MIMEText(str(message), _charset='utf-8')

    server = smtplib.SMTP(SMTP_HOST, 25)
    server.login(sender, "tsgowtbewkltjgfh")
    server.sendmail(sender, receivers, msg.as_string())


if __name__ == '__main__':
    send_mail()
