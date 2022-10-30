import email
from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGX = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        email_falg = UserProfile.objects.filter(email=postData['email'])
        if(email_falg):
            errors['emails_exist']="The email address that you entred exists before , please try to login with your email"
        if postData['email']!=postData['cemail']:
            errors['emails_not_identical']="Make sure Emails match"
        if postData['psw']!=postData['cpsw']:
            errors['psw_not_identical']="Make sure passwords match"
        if len(postData['mobile']) != 10:
            errors['mobile_len']="Number Of Valid Mobile Phone Digits Must Be 10"
        if len(postData['psw']) < 8 or len(postData['cpsw']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if not EMAIL_REGX.match(postData['email']) or not EMAIL_REGX.match(postData['cemail']):
            errors['not_valid_email']="Make sure that the email and confirmed email are valid"

        if len(errors) == 0:
            hashpw = bcrypt.hashpw(postData['psw'].encode(), bcrypt.gensalt()).decode()
            user_created= UserProfile.objects.create(email=postData['email'],password = hashpw,mobile_phone=postData['mobile'],location=postData['city'], delivery_address=postData['delivary-address'], first_name =postData['first-name'], last_name=postData['last-name'],purchase_count=0)
            user_created.save()
            errors['user_created']= user_created

        return errors



class UserProfile(models.Model):

    email = models.EmailField(max_length=254, null=False, blank=False) 
    password =models.CharField(max_length = 255)
    mobile_phone = models.CharField(max_length=20, null=False, blank=True)
    location = models.CharField(max_length=40, null=False,blank=True)
    delivery_address= models.CharField(max_length=200, null=False,blank=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    purchase_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    

