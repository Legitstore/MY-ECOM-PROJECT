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