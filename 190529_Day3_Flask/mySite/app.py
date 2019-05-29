from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    print(request.args) #ImmutableMultiDict([('user', '아라'), ('message', '흥흥흥')])
    name = request.args.get('user') #아라
    res_character = ['바보','못생김','이쁨','똑똑함','해맑음','식욕','인성','대충','분노','사악함','목소리','금','재물운','매력']
    dict_score = {}
    total = 0
    print(dict_score.keys())
    while total < 100:
        a = random.choice(res_character)
        s = random.randint(0,50)
        print(a,s)
        print(dict_score.keys())

        if a in dict_score.keys():
            dict_score[a] += s
        else:
            dict_score[a] = s

        total = total + s

        if total > 100:
            tmp = total - 100
            total -= tmp
            dict_score[a] -= tmp

    res = ''
    for item in dict_score:
        res += f' {item}: {dict_score[item]}%'

    print(dict_score.keys())

    return render_template('receive.html', name=name, result = str(res), color = "red")


@app.route('/lotto_result')
def lotto():
    #1. 내가 입력한 정보 가져오기
    lotto_round = request.args.get('lotto_round')
    my_numbers = request.args.get('my_nums')
    nums = my_numbers.split() #아무것도 입력안하면 space구분
    nums = set(map(int, nums))

    #2. 회차 정보 이용하여 로또 당첨 번호 가져오기
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    # print(response) #<Response [200]>
    lotto = response.json()
    # list comprehension
    winner = [ int(lotto[f'drwtNo{n}']) for n in range(1, 7)]
    bns = int(lotto['bnusNo'])
    res = f'{winner} + {bns}'

    #3. 당첨 여부 확인하기

    score = 0
    bns_score = 0
    li = []
    result =''

    ###### 반복문  ######
    # for i in nums:
    #     if i == bns:
    #         bns_score = 1
    #
    #     elif i in winner:
    #         score += 1
    #         li.append(i)

    ###### set 이용해서 교집합 구하기 ######  set -> {1.2.3.4}
    li = list(set(map(int, nums)) & set(map(int, winner)))   #교집합
    score = len(li)

    if score == 6:
        result = '축하합니다! 1등입니다.'

    elif score == 5:
        if bns in nums :
            bns_score = 1
            result = '축하합니다! 2등입니다.'
        else:
            result = '축하합니다! 3등입니다.'

    elif score == 4:
        result = '축하합니다! 4등입니다.'

    elif score == 3:
        result = '축하합니다! 5등입니다.'

    else:
        result = 'Bye... 이 다음에 또 만나용'

    # 4. 값전달
    return render_template('lotto_result.html'
                           , res=res
                           , lotto_round=lotto_round
                           , result = result
                           , my_nums = list(nums)
                           , score = score
                           , nums = li
                           , bns_score = bns_score
                           )

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/selectMenu')
def selectMenu():
    # selected = request.form['options']
    selected = request.args.get('options')

    if selected == 'god':
        url = 'send.html'
    else :
        url = 'lotto_check.html'

    return render_template(url)


if __name__ == '__main__':
    app.run(debug=True)


