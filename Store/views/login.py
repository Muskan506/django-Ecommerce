from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Store.models.product import Product
from django.contrib.auth.hashers import make_password,check_password
from Store.models.category import Category
from Store.models.customer import Customer
from django.views import View


class Login(View):
    def get(self,request):
        return render(request, 'login.html')


    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        print(customer)
        print(email, password)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
               # request.session['email']=customer.email
                return redirect('homepage')
            else:
                error_msg = "email or password invalid"
        else:
            error_msg = "email or password invalid"
        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('homepage')



