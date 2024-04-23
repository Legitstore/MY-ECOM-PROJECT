from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def homePage(request):
    return render(request, 'events/index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'events/collections.html', context)


def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'events/products/products.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            product = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'product': product}
        else:
            messages.warning(request, "No such product found")
            return redirect('collections')
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    
    return render(request, 'events/products/productview.html', context)