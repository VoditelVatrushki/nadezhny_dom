from django.shortcuts import render
 
 
def kontakty(request):
    """Страница контактов и форма обратной связи"""
    return render(request, 'kontakty.html')
