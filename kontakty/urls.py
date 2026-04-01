# kontakty/urls.py
from django.urls import path
from . import views

app_name = 'kontakty'

urlpatterns = [
    path('', views.kontakty, name='kontakty'),
]
