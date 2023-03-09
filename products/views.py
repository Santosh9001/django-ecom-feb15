from django.shortcuts import render,redirect
from django.views.generic import ListView
from products.models import Product
from django.http import HttpResponse, JsonResponse
import csv
from django.views.generic import View
from django.urls import reverse

from time import time

# Create your views here.

class Home(ListView):
    #  check if user is logged in 
    model = Product
    template_name='products/base.html'


# def myMiddleware(request):
#     return HttpResponse('Product page'+ str(request.current_time))


def exportcsv(request):
    products = Product.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Slug', 'Category', 'Preview Text','Detail Text','Price'])
    prods = products.values_list('id','name', 'slug', 'category', 'preview_text','detail_text','price')
    for prd in prods:
        writer.writerow(prd)
    return response


def entity_name(request):
    print("get from ajax")
    text = request.GET.get('button_text')
    print(text)
    t = time()
    # return JsonResponse(False,{'seconds': t},status=200)
    return HttpResponse(text)