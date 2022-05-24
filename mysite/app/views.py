from cgitb import html
from datetime import datetime
import datetime
from distutils import errors
from distutils.log import error
import re
from tkinter import Variable
from unicodedata import name
from urllib import request
from django.template import loader
from django import template
from datetime import timedelta 

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import Template,Context
from app.models import sign
from app.models import move
from app.models import jewel
from app.models import Itemcart
from django.contrib.auth import authenticate, login, logout
from django.contrib import sessions
from json import dumps

# Create your views here.

def home(request):
    desti = []
    curname = "default"
    desti = move.objects.all()
    print(desti)
    if request.session.get('username'):
        print(request.session.get('username'))
        try :
            curname  = (','.join(request.session['username']))
            img = sign.objects.get(uname = curname)
            return render(request, 'home.html', {
        'desti': desti,
        'img' : img.profile_pic
        })
        except:
            pass
 
   
    print("ok")
    return render(request, 'home.html', {
        'desti': desti,
        })
   

def signup(request):
    
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        uname = request.POST['uname']
        password = request.POST['password']
        print(fname,email,uname,password)
        ins = sign(fname=fname,email=email,uname=uname,password=password)
        ins.save()
        print("Data saved successfully")
    return render(request,'signup.html')



def logout(request):
    if request.session.get('username'):
      del request.session['username']
    request.session.modified = True
    return HttpResponseRedirect('/login/')
def moves(request):
    if request.method == "POST":
        url = request.POST['url']
        print(url)
        ins = move(url=url)
        ins.save()
        print("Data saved successfully")
    return render(request,'homebackground.html')

def jeweladd(request):
    if request.method == 'POST':
        jname = request.POST['jname']
        url = request.POST['url']
        price = request.POST['price']
        ins = jewel(jname=jname,url=url,price=price)
        ins.save()
        print("Data saved successfully")
    return render(request,'jewelsa.html')

def jewels(request):

    return render(request,'jewels.html')

def admincontrol(request):
    return render(request,'admincontroll.html')

def login(request):
    error = False
    if request.method == "POST":
        boole = False
        uname = request.POST['uname']
        password = request.POST['password']
        for each in sign.objects.all():
            if(each.uname == uname and each.password == password):
               
                request.session['username'] = [uname]
                print(request.session.get('username'))
                request.session.modified = True
                return HttpResponseRedirect('/home',{
                    #    error:
                })
            else:
                # errors.append('error')
                error=True
               
    return render(request,'login.html',{
        'ename' : "Invalid username or password ",
        'error':error
    })




def update(request):
    print("the method is",request.method)
    errors = False
    if(request.method == "POST"):
        print("Data updated successfully!")
        name=request.POST['uname']
        mail=request.POST['email']
        npassword=request.POST['npassword']
        sign.objects.filter(uname=name,email=mail).update(password=npassword)
        print("Data updated successfully!")
    else:
        errors=True
        print("No data found")

        
    return render(request,'update.html',{
        'ename' : "No data found ",
        'errors':errors
    })

def delete(request):
    if request.method == "POST":
        jname=request.POST['jname']
        dele=jewel.objects.get(jname=jname)
        dele.delete()
        print("Data deleted successfully")
    else:
        print("Redirected")
    return render(request,'jewelsd.html')

def profile(request):
    return render(request,'profile.html')
def index(request):
    return render(request,'index.html')

def bangle(request):
    count = 0
    for each in jewel.objects.all():
        if each.jname == "bangle":
            count = count+1
    data = {}
    i=0
    
    
    for each in jewel.objects.all():
        if each.jname == "bangle":
            data[i] = ([each.jname,each.url,each.price])
            i=i+1

    dataJSON =dumps(data) 
    return{
        'bang':dataJSON
    }

def cart(request):
    return render(request,'cart.html')

def datacart(request):
    if request.method == 'GET':
        dc_id = request.GET['p_id']
        obj = jewel.objects.get(id=dc_id)
        print(obj)
        jname = obj.jname
        jurl = obj.url
        jprice = obj.price
        d = Itemcart(icname=jname,icurl=jurl,icprice=jprice)
        d.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not GET") 

def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')