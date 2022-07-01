from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from numpy import save
from .models import product as Product
from .models import order as Order
from .forms import productForm,orderForm
from django.contrib.auth.models import User
from django.contrib import messages

#BY AMAN JAIN, BHASKARACHARYA COLLEGE OF APPLIED SCIENCES, DU
# Create your views here.

@login_required(login_url='user-login')
def index(request):

    orders=Order.objects.all()
    products=Product.objects.all()
    orders_count=orders.count()
    workers_count= User.objects.all().count()
    products_count=Product.objects.all().count()


    if request.method=='POST':
        form=orderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff=request.user
            instance.save()
            
            return redirect('dashboard-index')
    else:
        form = orderForm
   
    context = {
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count
    }
    return render(request,'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers= User.objects.all()
    workers_count=workers.count()
    orders_count=Order.objects.all().count()
    products_count=Product.objects.all().count()

    context ={
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count
    }
    return render(request,'dashboard/staff.html', context)

def staff_detail(request, pk):
     workers= User.objects.get(id=pk)
     context ={
        'workers':workers
     }
     return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request):

    #items = product.objects.all()
    items= Product.objects.raw('SELECT * FROM dashboard_product')
    count=0

    for i in items:
        count=count+1

    workers_count= User.objects.all().count()
    orders_count=Order.objects.all().count()
    products_count=count

    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added successfully!')
            return redirect('dashboard-product')

    else:
        form = productForm()

    context={
        'items':items, 
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request,'dashboard/product.html', context)

@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required(login_url='user-login')
def product_update(request, pk):
      item = Product.objects.get(id = pk)      

      if request.method == 'POST':
        form = productForm(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')

      else:
        form = productForm(instance=item)

      context={
        'form':form,

      }

      return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()
    orders_count=orders.count()
    workers_count= User.objects.all().count()
    products_count=Product.objects.all().count()

    context = {
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request,'dashboard/order.html', context)
