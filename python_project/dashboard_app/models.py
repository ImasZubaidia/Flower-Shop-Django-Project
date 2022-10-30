
import decimal
from operator import truediv
from pickle import FALSE, TRUE
from django.db import models
from login_app.models import UserProfile

class BouquetInventory(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=30, null=False, blank=True)
    product_image = models.URLField(max_length=1024, null=False, blank=True)
    in_stock = models.CharField(max_length=30, null=False, blank=True)
    sold_items = models.CharField(max_length=30, null=False, blank=True)
    discount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class OrderManager(models.Manager):
    def validate_order(self, postData,user,product):
        errors = {}
        if len(postData['receiver_name']) < 2:
            errors['password'] = "the receiver name you entred is so short please make sure you enter it correctly"

        if len(errors) == 0:
            units=int(postData['quantity'])
            
            product.in_stock =int(product.sold_items)-int(units)
            product.sold_items =int(product.sold_items)+int(units)
            product.unit =int(product.sold_items)-int(units)
            product.save()
            order_total = units* product.price + 20
            order_created= Order.objects.create(user_profile=user,address=postData['delivary-address'],delivery_date=postData["delivery-date"],delivery_cost=20,order_total=order_total,quantity=postData["quantity"],product=product,is_gift_wrapping=True,receiver_name=postData["receiver_name"],additional_notes=postData["notes"])
            order_created.save()
            errors['order_created']= order_created

        return errors

class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,null=True, blank=True,related_name='orders')
    address = models.CharField(max_length=250, null=False, blank=False)
    delivery_date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,null=False, default=0)
    order_total = models.DecimalField(max_digits=10,decimal_places=2, null=False, default=0)
    quantity = models.IntegerField()
    product = models.ForeignKey(BouquetInventory, on_delete=models.SET_NULL,null=True, blank=True,related_name='orders')
    is_gift_wrapping = models.BooleanField(blank=True)
    receiver_name = models.CharField(max_length=45)
    additional_notes = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OrderManager()



