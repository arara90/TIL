from django.shortcuts import render
import requests
import json
import random

def index(request):
    return render(request, 'utilities/index.html')
# Create your views here.

def requestpics(request):
    return render(request, 'utilities/requestpics.html')

def picsum(request):
    num = int(request.GET.get('num'))
    res = requests.get('https://picsum.photos/v2/list').text
    res = json.loads(res)
    print(num)

    li = random.sample(res, num)

    imgs = []
    for i in range(0, len(li)):
        imgs.append(li[i].get('download_url'))

    context = {'images': imgs}

    print(imgs)
    print(res)
    return render(request, 'utilities/picsum.html', context)


