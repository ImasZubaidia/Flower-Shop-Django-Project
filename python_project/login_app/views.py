from django.shortcuts import HttpResponse, redirect, render,HttpResponseRedirect

from login_app.models import UserProfile
from django.contrib import messages
import bcrypt
from django.http import JsonResponse

def login_render(request):
    return render(request, 'login.html')

def sign_me_in(request):
    current_user_email=request.POST["email"]
    current_user_password=request.POST["psw"]
    user = UserProfile.objects.filter(email= current_user_email) 
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(current_user_password.encode(), logged_user.password.encode()):
            request.session['email'] = logged_user.email
            return redirect('/')
        else:
            messages.error(request,"Invalid Password")
            return redirect(login_render)
    else:
        messages.error(request,"The email address doesn't belong to any Account , not a member yet? Join our family ")
        return redirect(login_render)



def registration(request):
    return render(request, 'registration.html')


def register_me(request): 

    errors = UserProfile.objects.reg_validator(request.POST)
    if 'user_created' in errors:
        request.session['email'] = errors['user_created'].email
        request.session['name'] = errors['user_created'].first_name
        request.session['record'] = "registered!"
        return redirect('/')    
    else:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(registration)


