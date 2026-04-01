# nadezhny_dom_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),         # namespace: homepage
    path('uslugi/', include('uslugi.urls')),    # namespace: uslugi
    path('cart/', include('cart.urls')),        # namespace: cart
    path('kontakty/', include('kontakty.urls')),  # namespace: kontakty
]
