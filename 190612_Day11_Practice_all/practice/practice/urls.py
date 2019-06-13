"""practice URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
]

# 기존 static 이미지는 {% load static %}으로 불러올 수 있었다.
# STATICFILES_DIRS 참고해서..
# 얘처럼 user가 올린 이미지도 어디에 위치했는지 주소를 부여해주어야한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
