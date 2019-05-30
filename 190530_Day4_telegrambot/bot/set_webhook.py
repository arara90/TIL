from flask import Flask, render_template, request
import requests
import random
from decouple import config

app = Flask(__name__)
token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

# cmd에서 # ngrok localhost 5000 명령어(홈페이지 참고 5000은 port)
# flask_url = f'https://e2386e03.ngrok.io/{token}'
flask_url = f'https://arara90.pythonanywhere.com/{token}'
# telegram한테도 토큰이 있는 주소로 알려달라고 요청하는 것.

# 전파해줌?
set_url = f'{api_url}/setWebhook?url={flask_url}'
response = requests.get(set_url)
print(response.text)



# is는 메모리 비교, 많이 쓰는 -5~255는 미리 올려놓고 해당 메모리 주소 가져온다.
# ==은 값비교
# is none : none은 메모리 상에 단 하나만 존대
# 문자열은 == 으로 비교