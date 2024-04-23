from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import ProdForm, CateForm

# Create your views here.
def homePage(request):
    trending_collections = Category.objects.filter(trending=True)
    trending_products = Product.objects.filter(trending=True)
    context = {'trending_products': trending_products,
               'trending_collections': trending_collections
               }
    return render(request, 'events/index.html', context)

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

def collectform(request):
    if request.method == 'POST':
        form = CateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            collect_name = form.cleaned_data.get('name')
            messages.success(request, f'{collect_name} has been added')
            return redirect('collectform')
    else:
        form = CateForm()
    context = {'form': form}
    return render(request, 'events/collectionsform.html', context)


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

def productform(request):
    # cateforms = CateForm()

    if request.method == 'POST':
        form = ProdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('productform')
    else:
        form = ProdForm()
    context = {'form': form}
    return render(request, 'events/products/productform.html', context)