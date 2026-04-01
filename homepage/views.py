# homepage/views.py
from django.shortcuts import render


def index(request):
    """Главная страница — передаём данные через context."""
    context = {
        'page_title': 'Строительная компания «Надёжный дом»',
        'promo_active': True,
        'promo_text': 'Скидка 15% на строительство домов при заключении договора до 31 декабря',
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def prices(request):
    return render(request, 'prices.html')


def kalkulyator(request):
    return render(request, 'kalkulyator.html')


def reviews(request):
    return render(request, 'reviews.html')


def cabinet(request):
    return render(request, 'cabinet.html')
