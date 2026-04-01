# homepage/urls.py
from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('prices/', views.prices, name='prices'),
    path('kalkulyator/', views.kalkulyator, name='kalkulyator'),
    path('reviews/', views.reviews, name='reviews'),
    path('cabinet/', views.cabinet, name='cabinet'),
]
