from django.shortcuts import render, redirect
from .models import Product,Make
from django.contrib import messages
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
    if request.method == 'POST':
        name_product = request.POST.get('name_product','')
        make = request.POST.get('make','')
        price = request.POST.get('price','')
        county = request.POST.get('county','')
        create_at = request.POST.get('create_at','')
        desc = request.POST.get('desc','')
        image = request.FILES['image']


        product = Product(
            name_product=name_product,
            make=make,
            price=price,
            county=county,
            create_at=create_at,
            desc=desc,
            image=image,
        )

        product.save()


        redirect('full',product.pk)

    return render(request,'create_product.html')

