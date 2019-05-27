import requests
from bs4 import BeautifulSoup as bs
import datetime

html = requests.get('http://www.naver.com').text
soup = bs(html, 'html.parser')
ranks = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
now = datetime.datetime.now()

with open('naver_rank.txt', 'w', encoding='UTF-8') as f:
    f.write(f'{now} 기준 네이버 검색어\n')
    for i, rank in enumerate(ranks):
        #enumerate(ranks) index정보도 추가해서 졸린다. i에는 인덱스를.
        f.write(f'{i+1}. {rank.text} \n')
