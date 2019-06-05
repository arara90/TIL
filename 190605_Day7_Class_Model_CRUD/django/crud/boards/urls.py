from django.contrib import admin
from django.urls import path
from . import views

#작성방향 : 새로운 것이 아래로 ↓
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create)
]
