# uslugi/urls.py
from django.urls import path
from . import views

app_name = 'uslugi'  # namespace = имя приложения

urlpatterns = [
    path('', views.uslugi_list, name='uslugi_list'),
    path('<int:pk>/', views.uslugi_detail, name='uslugi_detail'),
]
