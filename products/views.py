from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from django.utils import timezone

def home(request):
    Product = models.Product.objects.all()
    return render(request,"products/home.html", {'products':Product})

@login_required 
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            Product = models.Product()
            Product.title       = request.POST['title']
            Product.body        = request.POST['body']
            Product.url         = request.POST['url']
            Product.image       = request.FILES['image']
            Product.icon        = request.FILES['icon']
            Product.pub_date    = timezone.datetime.now()
            Product.votes_total = 1
            Product.customer    = request.user           
            Product.save()
            print('product saved')
            return redirect('/products/'+str(Product.id))
        else :
            return render(request,'products/create.html' ,{'error':'All fields are required'})

    return render(request,'products/create.html')

def detail(request, product_id):
    Product = get_object_or_404(models.Product, pk=product_id)
    return render(request,'products/detail.html',{'product':Product})

@login_required(login_url='/accounts/signup')
def upvote(request, product_id):
    if request.method == 'POST' :
        Product = get_object_or_404(models.Product, pk=product_id)
        Product.votes_total += 1
        Product.save()
        print("SAVE")
        return redirect('/products/'+str(Product.id))