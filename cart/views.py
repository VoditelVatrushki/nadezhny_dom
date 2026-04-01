from django.shortcuts import render
 
 
def cart_view(request):
    """
    Страница корзины заказов.
    Данные корзины хранятся в localStorage браузера —
    сервер только отдаёт HTML-шаблон.
    """
    return render(request, 'cart.html')
