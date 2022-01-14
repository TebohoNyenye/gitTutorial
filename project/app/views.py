from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder



# Create your views here.

class HomeView(TemplateView):
    
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

def ProductView(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request,'Products.html',context)  
    
   
       

class CartView(TemplateView):
    template_name = "cart.html"


