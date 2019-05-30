import requests
import random

token = '663899527:AAHyZWnizopIR45o5GXn06YZx2r63toAhT4'
api_url = f'https://api.telegram.org/bot{token}'

#https://api.telegram.org/bot663899527:AAHyZWnizopIR45o5GXn06YZx2r63toAhT4/getUpdates 에서 내 계정id 확인
# from -> id : 894138210 (내 계정)

chat_id = '894138210'


# sendMessage
#text = input('메시지 입력')
text = random.sample(range(1,46), 6)
url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
print(url)

response = requests.get(url)
print(response)
