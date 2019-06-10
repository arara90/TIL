from django.contrib import admin
from django.urls import path
from . import views

#작성방향 : 새로운 것이 아래로 ↓
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update)
]
