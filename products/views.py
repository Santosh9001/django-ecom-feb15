from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.http import HttpResponse

# Create your views here.

class Home(ListView):
    #  check if user is logged in 
    model = Product
    template_name='products/home.html'


# def myMiddleware(request):
#     return HttpResponse('Product page'+ str(request.current_time))