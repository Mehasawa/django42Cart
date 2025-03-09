from datetime import timezone

from django.shortcuts import render,redirect
from .models import *
from .forms import *
import datetime
# Create your views here.

def index(request):
    items = Tovar.objects.all()
    data={'items':items}
    return render(request, 'index.html',data)

def catalog(request,cat):
    items = Tovar.objects.filter(category__name=cat)
    data={'items':items}
    return render(request, 'index.html',data)

def cart(request):
    items = Cart.objects.filter(user_id=request.user.id)
    total = 0
    form = OrderForm()
    sps=''
    for one in items:
        total+=one.summa
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            k1 = form.cleaned_data['adres']
            k2 = form.cleaned_data['telephone']
            zakaz=''
            for one in items:
                zakaz+=one.tovar.name + ' '+ str(one.count)+ ' '+str(one.summa) + '\n'
            zakaz+='Всего '+ str(total) + '\n'
            zakaz += 'Адрес ' + k1 + '\n'
            zakaz += 'Телефон ' + k2 + '\n'
            zakaz += 'Пользователь ' + request.user.username + '\n'
            status = Status.objects.get(id=1)
            Order.objects.create(adres=k1,tel=k2, user_id=request.user.id,
                                 total=total, status=status,
                                 zakaz=zakaz, email=request.user.email,
                                 date=datetime.datetime.now())
            items.delete()
            total = 0
            sps = 'Спасибо за заказ'
    data = {'items': items, 'total': total, 'form':form, 'sps':sps}
    return render(request, 'cart.html',data)

def cabinet(request):
    orders = Order.objects.filter(user_id=request.user.id)
    data = {'orders':orders}
    return render(request, 'cabinet.html',data)

def buy(request,cat,itemid):
    item = Tovar.objects.get(id=itemid)
    user = request.user.id
    print(user,item)
    if Cart.objects.filter(user_id=user,tovar_id=item.id):
        item = Cart.objects.get(user_id=user,tovar_id=item.id)
        item.count+=1
        item.summa = item.calcSumma()
        item.save()
    else:
        Cart.objects.create(user_id=user,tovar_id=item.id,count=1,
                            summa=item.price)
    return redirect('catalog',cat)

def delete(request,itemid):
    item = Cart.objects.get(id=itemid)
    item.delete()
    return redirect('cart')

def edit(request,itemid,num):
    item = Cart.objects.get(id=itemid)
    num = int(num)
    item.count += num
    item.summa = item.calcSumma()
    if item.count > 0:
        item.save()
        return redirect('cart')
    else:
        return redirect('delete', itemid)

