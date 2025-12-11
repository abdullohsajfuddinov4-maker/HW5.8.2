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

from django.shortcuts import render, redirect
from .models import Product, Make

def create_product(request):
    if request.method == 'POST':
        name_product = request.POST.get('name_product', '')
        make = Make.objects.filter(name=request.POST.get('make', '')).first()
        price = request.POST.get('price', '')
        county = request.POST.get('county', '')
        desc = request.POST.get('desc', '')
        image = request.FILES.get('image')

        product = Product(
            name_product=name_product,
            make=make,
            price=price,
            county=county,
            desc=desc,
            image=image,
        )
        messages.success(request,'product qoshildi')
        product.save()

        return redirect('full', pk=product.pk)

    return render(request, 'create_product.html')



def updata_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.name_product = request.POST.get('name_product', '')
        make_name = request.POST.get('make', '')

        make_instance = Make.objects.filter(name=make_name).first()
        if make_instance:
            product.make = make_instance
        product.price = request.POST.get('price', 0)
        product.county = request.POST.get('county', '')
        product.desc = request.POST.get('desc', '')
        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        return redirect('full', pk=product.pk)


    return render(request, 'updata.html', {'product': product})


def del_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request,'del_product.html',{'product':product})

