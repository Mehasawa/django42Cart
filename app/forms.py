from django.forms import Form
from django import forms

class OrderForm(Form):
    adres = forms.CharField(label='Адрес доставки')
    telephone = forms.CharField(label='Телефон')
    nerobot = forms.BooleanField(label='не робот')