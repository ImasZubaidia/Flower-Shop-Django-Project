
from itertools import product
from multiprocessing import context
from unicodedata import category
from unittest import result
from django.shortcuts import render,redirect
from dashboard_app.models import BouquetInventory, Order
from django.http import HttpResponse
from login_app.models import UserProfile
from django.contrib import messages

def index(request):
    return render(request ,'index.html')

def aboutus(request):
    return render(request,'about.html')

def anniversary(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='Anniversary')
    }
    return render(request, 'anniversary.html',context)


def congrats(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='Congrats')
    }
    return render(request, 'congrats.html',context)

def single_flower(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='Single Flower')
    }
    return render(request, 'single_flower.html',context)

def sympathy_and_funerals(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='Sympathy and Funerals')
    }
    return render(request, 'sympathy_and_funerals.html',context)


def birthday(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='Birthday')
    }
    return render(request, 'birthday.html',context)

def cheer_someone_up(request):
    context = {
        "products_list" : BouquetInventory.objects.filter(category='cheer someone up')
    }
    return render(request, 'cheer_someone_up.html',context)

def top_ten(request):
    dec_list = BouquetInventory.objects.all().order_by("-sold_items")
    top_10 = get_top_ten(dec_list)
    context = {
        "products_list" : top_10
        }
    return render (request, 'top_ten.html',context)

def about_us(request):
    return render (request,'about.html')

def new_arrivals(request):
    dec_list = BouquetInventory.objects.all().order_by("-created_at")
    context = {
        "products_list" : dec_list
        }
    return render (request,'new_arrivals.html',context)

def all_flowers(request):
    context = {
        "products_list" : BouquetInventory.objects.all()
    }
    return render(request,'all_flowers.html',context)

def logout(request):
	request.session.clear()
	return redirect('/')

def my_orders_list(request):

    if("email" not in request.session):
         messages.error(request,"Please login first to be able to see your orders list")
         return render (request, 'my_orders.html')
    else:
        user_signed =request.session['email']
        user = UserProfile.objects.filter(email= user_signed)  
        context = {
        "orders_list" : Order.objects.filter(user_profile=user[0])
        }
        return render (request, 'my_orders.html',context)


    
    
def book_now(request,product_id):
    context ={
        "product":BouquetInventory.objects.get(id=product_id)
    }
    return render(request,"book_now.html",context)


def create_order(request,product_id):

    if("email" not in request.session):
         messages.error(request,"Please login first and then send your order")
         return render(request,"book_now.html")
    else:
        user_signed =request.session['email']
        user = UserProfile.objects.filter(email= user_signed) 
        ordered_product= BouquetInventory.objects.get(id=product_id)
        if user:
            logged_user = user[0] 
            errors = Order.objects.validate_order(request.POST,logged_user,ordered_product)
            if 'order_created' in errors:
                return redirect('/')         
            else:
                for key, value in errors.items():
                    messages.error(request, value)
                return render(request,"book_now.html")

def delete_order(request,order_id):
    order = Order.objects.get(id=order_id)	
    order.delete()	
    return redirect(my_orders_list)



def get_top_ten(list):
    result=[]
    for num in range(1, 11):
        result.append(list[num])
    return result