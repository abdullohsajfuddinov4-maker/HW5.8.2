from django.shortcuts import render
from .models import Product,Make
# Create your views here.

def home(request):
    make = Make.objects.all()
    context = {'make':make}
    return render(request,'home.html',context)

def product(request,pk):
    products = Product.objects.filter(make__id=pk)
    context = {'products':products}
    return render(request,'product.html',context)

def desc(request,pk):
    products = Product.objects.filter(pk=pk)
    context = {'products':products}
    return render(request,'desc.html',context)

def create_product(request):
