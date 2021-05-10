from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Store.models.product import Product
from django.contrib.auth.hashers import make_password,check_password
from Store.models.category import Category
from Store.models.customer import Customer

from Store.models.product import Product
from django.views import View



class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        return render(request, 'cart.html',{'products':products})

