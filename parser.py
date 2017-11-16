import requests
from bs4 import BeautifulSoup as bs
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

#BlogData를 import해옵니다
from blog.models import BlogData

def parse_blog():
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html = req.text
    soup = bs(html, 'html.parser')
    my_titles = soup.select('h3 > a')
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data

if __name__=='__main__':
    blog_data_dict = parse_blog()
    for t, l in blog_data_dict.items():
        BlogData(title=t, link=l).save()

#HTTP GET request
# req = requests.get('https://beomi.github.io/')
#
# #HTML 소스 가져오기
# html = req.text
# #HTML Header 가져오기
# header = req.headers
# #HTTP Status 가져오기(200:정상)
# status = req.status_code
# #HTTP가 정상적으로 되었는지 (True/False)
# is_ok = req.ok
#
# #Python파일의 위치
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# #BeautifulSoup으로 html소스를 python 객체로 변환하기
# #첫 인자는 html소스코드, 두번째 인자는 어떤 parser를 이용할지 명시.
# #이 글에서는 Python 내장 html.parser를 이용했다.
# soup = bs(html, 'html.parser')
# #CSS Selector를 통해 html요소들을 찾아낸다.
# my_titles = soup.select('h3 > a')
#
# data = {}
# #my_titles는 list 객체
# for title in my_titles:
#     #Tage안의 텍스트
#     # print(title.text)
#     #Tag의 속성을 가져오기(ex: href속성)
#     # print(title.get('href'))
#     data[title.text] = title.get('href')
#
# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)
