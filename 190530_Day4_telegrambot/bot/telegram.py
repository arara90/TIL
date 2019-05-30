import requests
import random
from decouple import config

token = config('TELE_TOKEN')
api_url = f'https://api.telegram.org/bot{token}'
chat_id = config('CHAT_ID')
# https://api.telegram.org/bot663899527:AAHyZWnizopIR45o5GXn06YZx2r63toAhT4/getUpdates 에서 내 계정id 확인
# from -> id


# sendMessage
# text = input('메시지 입력')
text = random.sample(range(1,46), 6)
url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
print(url)

response = requests.get(url)
print(response)
