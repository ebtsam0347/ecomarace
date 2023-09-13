from django.shortcuts import render

def index(request):
    return render(request, 'ebrand/index.html')

def cart(request):
    return render(request, 'ebrand/cart.html')

def detail(request):
    return render(request, 'ebrand/detail.html')

def shop(request):
    return render(request, 'ebrand/shop.html')

def checkout(request):
    return render(request, 'ebrand/checkout.html')

def contact(request):
    return render(request, 'ebrand/contact.html') 

def login(request):
    return render(request, 'ebrand/login.html')
    
def register(request):
    return render(request, 'ebrand/register.html')
