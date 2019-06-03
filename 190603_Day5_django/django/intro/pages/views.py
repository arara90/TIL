from django.shortcuts import render
import random
from datetime import datetime,timedelta

# Create your views here.
def index(request):
    return render(request, 'index.html')


def hola(request):
    return render(request, 'hola.html')


def dinner(request):
    menu = ['족발', '삼겹살', '냉면', '치맥', '피자', '양고기', '다이어트!!!!']
    pick = random.choice(menu)
    context = {'pick':pick}
    #return render(request, 'dinner.html', {'pick': pick})
    return render(request, 'dinner.html', context)

def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

def introduce(request, name, age):
    context = {'name': name , 'age': age}
    return render(request, 'introduce.html', context)

def times(request, num1, num2):
    context = {'num1':num1, 'num2': num2, 'res':  num1 * num2 }
    return render(request, 'times.html', context)

def circle(request, r):
    context = {'r': r, 'res': (r**2) * 3.14}
    return render(request, 'circle.html', context)


def template_language(request):
    menus = ['족발', '삼겹살', '냉면', '치맥', '피자', '양고기', '다이어트!!!!']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'mango']
    empty_list = ['좌롸','롸', '좌라']
    datatimenow = datetime.now()
    print(datatimenow)
    context = {
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':messages,
        'empty_list':empty_list,
        'datatimenow':datatimenow
    }

    return render(request, 'template_language.html', context)

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
    return render(request, 'birthday.html', context)


def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message1 = request.GET.get('message1')
    message2 = request.GET.get('message2')
    # message = request.GET['message']
    # request.Get['key'] 는 일치하는 key가 없을 때, error지만 .get 접근시에는 error 안난다.
    # Flask에서는 arg : lotto_round = request.args.get('lotto_round')
    # C:\Users\multicampus\TIL\190529_Day3_Flask\mySite\app.py

    context = {'message1': message1 , 'message2': message2}
    return render(request, 'catch.html', context)
