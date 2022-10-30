from atexit import register
from django.urls import path 
from . import views

urlpatterns = [
    path('/login', views.login_render ),
    path('/registration', views.registration),
    path('/sucess', views.sign_me_in),
    path('/register_me',views.register_me),
]


