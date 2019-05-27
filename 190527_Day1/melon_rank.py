import requests
import bs4

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
#print(response)
soup = bs4.BeautifulSoup(response, 'html.parser')
songs = soup.select('#lst50')


#406
# request 사용 시, 요청에 운영체제, 브라우저 정보등을 담아 보내지 않는다. 의심스러워 -> 응답안해줌.
# sol) header에 정보를 담아 보내자
# F12 - > network -> headers -> 왼쪽 Names에서 아무거나 클릭 -> request Headers

with open('melon_rank.csv', 'w', encoding='utf-8') as f:
    for song in songs:
        rank = song.select_one('td:nth-child(2) > div > span.rank').text
        title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text

        f.write(f'{rank}위, {title}  by.{artist} \n')
