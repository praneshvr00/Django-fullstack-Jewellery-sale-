from django.contrib import admin
from app.models import sign 
from app.models import move
from app.models import jewel
from app.models import Itemcart

#models - DB
# Register your models here.

admin.site.register(sign)
admin.site.register(move)
admin.site.register(jewel)
admin.site.register(Itemcart)