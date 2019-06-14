"""ARA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:board_pk>/', views.detail, name='detail'),
    path('<int:board_pk>/edit/', views.edit, name='edit'),
    path('<int:board_pk>/delete/', views.delete, name='delete'),

    path('<int:board_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:board_pk>/comments/<int:comment_pk>/edit/', views.comments_edit, name='comments_edit'),
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete')
]

##RESTFul? REST(Representational State Transfer)Ful
## uri는 자원만 표현 , 작업은 명시적으로 표현 /edit..

## method는 작업 (edit, update)를 하나로 합침
## action=""
## 자기자신이 호출된 그 경로(함수)로 다시 한 번 요청을 보낸다.
