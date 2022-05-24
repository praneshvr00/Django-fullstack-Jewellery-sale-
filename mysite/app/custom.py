import re
from app.models import sign , jewel ,Itemcart
from json import dumps
def status(request):
    if request.session.get('username'):
        try :
            curname  = (','.join(request.session['username']))
            img = sign.objects.get(uname = curname)
            return {
        'img' : img.profile_pic,
        'status' : True,
        }
        except:
            pass
    return({
            'status' : False
        })
# def banglepass(request):
#     count = 0
#     for each in jewel.objects.all():
#         if each.jname == "bangle":
#             count = count+1
#     data = {}
#     i=0
#     # data = jewel.objects.filter(jname="bangle")
    
#     for each in jewel.objects.all():
#         if each.jname == "bangle":
#             data[i] = ([each.jname,each.url,each.price])
#             i=i+1

#     dataJSON =dumps(data) 
#     return{
#         'data':dataJSON
#     }

def banglepass(request):
    l = []
    l = jewel.objects.filter(jname="bangle")
    return {
        'bangle' : l,
    }

def chainpass(request):
    l = []
    l = jewel.objects.filter(jname="chain")
    return {
        'chain' : l,
    }

def allpass(request):
    l = []
    l = jewel.objects.all()
    return {
        'all' : l,
    }

def cartdata(request):
    data = Itemcart.objects.all()
    return{
        'cartdata' : data,
    }
