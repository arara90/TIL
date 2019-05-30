from flask import Flask, render_template, request
import requests
import random
from decouple import config

app = Flask(__name__)

#1.telegram
token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
chat_id = config('CHAT_ID')

#2.naver
NAVER_CLIENT_ID = config('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = config('NAVER_CLIENT_SECRET')
papago_url = 'https://openapi.naver.com/v1/papago/n2mt'


# API url 주소값
api_url = f'https://api.telegram.org/bot{token}'


## 웹페이지 만들기
# 프론트 페이지
# #POST방식으로만 받을 수 있다 : 보안적으로 보다 안전한 서버를 만들 수 있다. (get방식은 주소에 노출)
@app.route(f'/{token}', methods=['POST'])
def telegram():

    # 딕셔너리에서 key값 가져오는 방법
    # 1. lotto['key'] => value, 'key'가 없다면 에러 발생!
    # 2. lotto.get('key') => value, 'key'가 없다면 None 리턴!

    message = request.get_json().get('message')

    print(message)

    # 보낸 사람 id
    if message is not None :
        chat_id = message.get('from').get('id')

        # 보낸 사람에게 받은 메시지
        text = message.get('text')
        print(text)
        if text == '로또':
            text = random.sample(range(1,47), 6)

        # 네이버 번역 : POST > 헤더에 Id, secret을 담아 보낸다. / 데이터는 따로 담아 보낸다.


        print(text[0:4])
        if text[0:4].rstrip() == '/번역':
            headers = {
                'X-Naver-Client-Id': NAVER_CLIENT_ID,
                'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
            }

            data = {
                'source': 'ko',
                'target': 'en',
                'text': text[4:]
            }

            papago_res = requests.post(papago_url, headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText')


        # 보낸 사람에게 다시 메시지 보내기
        send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'

        # sendMessage 요청 보내기
        response = requests.get(send_url)

    return '', 200  # '': 응답을 받을 메시지 / 200: 응답코드(Status Code)

# .get('result').get('translatedText')

if __name__ == '__main__':
    app.run(debug=True)



#
# # 우리 서버가 여기에있다! 어떻게 알려줭? 원래는 고정IP 필요.
# # ngrok (엔그록)
# # localhost서버를 외부에 임시로 연결해주는 것. (임시 발급)
# # https://dashboard.ngrok.com/get-started
# if __name__ == '__main__' :
#