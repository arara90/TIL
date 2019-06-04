from django.shortcuts import render
import random
from datetime import datetime,timedelta
import json
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def hola(request):
    return render(request, 'pages/hola.html')


def dinner(request):
    menu = ['족발', '삼겹살', '냉면', '치맥', '피자', '양고기', '다이어트!!!!']
    pick = random.choice(menu)
    context = {'pick': pick}
    #return render(request, 'dinner.html', {'pick': pick})
    return render(request, 'pages/dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'pages/hello.html', context)

def introduce(request, name, age):
    context = {'name': name , 'age': age}
    return render(request, 'pages/introduce.html', context)

def times(request, num1, num2):
    context = {'num1': num1, 'num2': num2, 'res':  num1 * num2 }
    return render(request, 'pages/times.html', context)

def circle(request, r):
    context = {'r': r, 'res': (r**2) * 3.14}
    return render(request, 'pages/circle.html', context)


def template_language(request):
    menus = ['족발', '삼겹살', '냉면', '치맥', '피자', '양고기', '다이어트!!!!']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'mango']
    empty_list = ['좌롸', '롸', '좌라']
    datatimenow = datetime.now()
    print(datatimenow)
    context = {
        'menus':menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datatimenow': datatimenow
    }

    return render(request, 'pages/template_language.html', context)

def isbirth(request,birthday):

    mybirthday = datetime.strptime(birthday, '%Y-%m-%d').date()
    now = datetime.now().date()
    mybirthday_thisyear = mybirthday.replace(now.year, mybirthday.month, mybirthday.day)

    #print(mybirthday.strftime('%m%d'))
    #print(now.strftime('%m%d'))
    #print(bool( mybirthday.strftime('%m%d') == now.strftime('%m%d') ))

    if mybirthday_thisyear == now:
        dday = f'D-Day!!'

    else:
        if mybirthday_thisyear > now:
            nextbirthday = mybirthday_thisyear
            dday = f'D - {(nextbirthday - now).days}'
        else:
            nextbirthday = mybirthday.replace(now.year + 1, mybirthday.month, mybirthday.day)
            dday = f'D - {(nextbirthday - now).days}'

    res = (mybirthday.month == now.month) & (mybirthday.day == now.day)
    #res = mybirthday.strftime('%m%d') == now.strftime('%m%d')

    context = {'res': res, 'dday': dday}
    return render(request, 'pages/birthday.html', context)


def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    # message = request.GET['message']
    # request.Get['key'] 는 일치하는 key가 없을 때, error지만 .get 접근시에는 error 안난다.
    # Flask에서는 arg : lotto_round = request.args.get('lotto_round')
    # C:\Users\multicampus\TIL\190529_Day3_Flask\mySite\app.py

    context = {'message1': message1 , 'message2': message2}
    return render(request, 'pages/catch.html', context)

def get(request):
    name = request.GET.get('name')
    lotto = range(1, 46)
    nums = sorted(random.sample(lotto, 6))

    context = {'name': name,
               'nums': nums}
    return render(request, 'pages/get.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto2(request):
    return render(request, 'pages/lotto2.html')

def picklotto(request):
    name = request.GET.get('name')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=861')
    lotto = json.loads(res.text)
    print(lotto)

    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'] )

    picked = sorted(random.sample(range(1, 46), 6))

    #set의 활용 : 집합(특히 교집합), 중복 제거
    matched = len(set(winner) & set(picked))

    if matched == 6 :
        result = "1등입니다. "
    elif matched == 5 :
        result = "3등입니다. 휴가 고고"
    elif matched == 4 :
        result = "4등입니다. 맛난거 머거용 고고"
    elif matched == 3 :
        result = "5등입니다. 넣어둬"
    else :
        result = "설마 기대한건 아니죠? ㅉㅉ.."

    context = {'name': name, 'result': result}

    return render(request, 'pages/picklotto.html', context)

def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form 태그로 날린 데이터를 받는다.
    word = request.GET.get('word')

    #2. artii API를 통해 보낸 응답 결과를 text로 fonts에 저장
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    print(fonts)

    #3. fonts(str)를 font 리스트의 형태로 저장한다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font에 저장
    font = random.choice(fonts)

    print(word, font)

    # 사용자에게 받은 word와 랜덤하게 뽑은 font를 가지고 다시 요청을 보낸다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    print(result)

    context = {'result': result}
    return render(request, 'pages/result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")

    context = {'name': name, 'pwd': pwd}
    return render(request, 'pages/user_create.html', context)

def static_example(request):
    return render(request, 'pages/static_example.html')