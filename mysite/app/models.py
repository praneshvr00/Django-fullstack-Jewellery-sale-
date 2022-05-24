from email.policy import default
from pyexpat import model
from tokenize import blank_re
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class sign(models.Model):
    fname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/profiles', default='images/profiles/default.png')
    gender = models.CharField(max_length=100)
    dob = models.DateTimeField(null=True,blank=True)
    address = models.CharField(max_length=200,default="Your address")
   

class move(models.Model):
    url = models.CharField(max_length=500)

class jewel(models.Model):
    id=models.IntegerField(primary_key=True)
    jname = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    
class Itemcart(models.Model):
    icname = models.CharField(max_length=100)
    icurl = models.CharField(max_length=500)
    icprice = models.CharField(max_length=100)
 
def __unicode__(self):        #if error use this function
    return self.name 