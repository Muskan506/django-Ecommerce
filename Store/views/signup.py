# from django.views import View
from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from store.models.product import Product
from django.contrib.auth.hashers import make_password, check_password
# from Store.models.category import Category
from Store.models.customer import Customer
# from django.views import View


def signup(request):
    error_msg = None
    # msg_er = None
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')
    value = {'first_name': first_name,
             'last_name': last_name,
             'phone': phone,
             'email': email,
             # 'password': password
             }
    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        email=email, password=password,
                        phone=phone)

    if (not first_name):
        error_msg = " first name required"
    elif len(first_name) < 4:
        error_msg = "first name must be 4 char long"
    elif (not last_name):
        error_msg = "last name required"
    elif len(last_name) < 4:
        error_msg = "last name must be 4 char  long"
    elif (not email):
        error_msg = "emil required"
    elif len(email) < 5:
        error_msg = "email must be 4 char long"

    elif (not phone):
        error_msg = "phone is required"
    elif len(phone) < 10:
        error_msg = "phone no is must be 10 char long"
    elif  not phone.isnumeric():
        error_msg="plz enter only numeric value"

    elif (not password):
        error_msg = "password is required"
    elif len(password)<6:
        error_msg="password must be 6 char long"
    elif customer.isExists():
        error_msg = "email already exists!!"

    if not error_msg:
        # msg=None
        customer.password = make_password(customer.password)
        customer.register()

        return redirect('login')
    else:
        data = {
            'error': error_msg,
            'values': value
        }
        return render(request, 'signup.html', data)
