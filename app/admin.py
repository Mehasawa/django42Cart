from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Status)
admin.site.register(Category)

class adminTovar(admin.ModelAdmin):
    list_display = ('name','price','discount','category')

admin.site.register(Tovar,adminTovar)

class adminOrder(admin.ModelAdmin):
    list_display = ('date','user')

admin.site.register(Order,adminOrder)

class adminCart(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Cart,adminCart)