from django.urls import path

from cart.views import generatePDF, add_to_cart, remove_from_cart,CartView,decreaseCart
from .views import Home, exportcsv,entity_name

app_name = 'mainapp'

urlpatterns = [
    path('page',Home.as_view(),name='home'),
    path('cart', CartView, name='cart-home'),
    path('cart/<slug>',add_to_cart,name='cart'),
    path('remove/<slug>',remove_from_cart,name='remove-cart'),
    path('decrease-cart/<slug>', decreaseCart, name='decrease-cart'),
    path('cart/<int:id>/generatePDF/',generatePDF,name='generatePDF'),
    path('exportcsv',exportcsv),
    path('entity_name',entity_name,name='entity_name')
]