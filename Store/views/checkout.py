from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Store.models.product import Product
from django.contrib.auth.hashers import make_password,check_password
from Store.models.category import Category
from Store.models.customer import Customer
from Store.models.orders import Order

from Store.models.product import Product
from django.views import View



class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        for product in products:
            print(cart.get(str(product.id)))
            order=Order(customer=Customer(id=customer),
                        product=product,
                        price=product.price,
                        address=address,
                        phone=phone,
                        quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart']={}
        return redirect('Cart')
