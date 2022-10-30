from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('anniversary', views.anniversary),
    path('congrats', views.congrats),
    path('single_flower', views.single_flower),
    path('sympathy_and_funerals', views.sympathy_and_funerals),
    path('birthday', views.birthday),
    path('cheer_someone_up', views.cheer_someone_up),
    path('top_ten', views.top_ten),
    path('about_us', views.about_us),
    path('new_arrivals', views.new_arrivals),
    path('all_flowers', views.all_flowers),
    path('log_out', views.logout),
    path('my_orders_list', views.my_orders_list),
    path('book_now/<int:product_id>', views.book_now),
    path('book_item_for_me/<int:product_id>',views.create_order),
    path('delete_order/<int:order_id>',views.delete_order)
    

]

