from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.


def home(request):
    list_custumer = Custumer.objects.order_by('id')
    list_order = Order.objects.order_by('-id')
    # .count berfungsi untuk mencari dan mengetahui total table dari list_order
    total_order = list_order.count()
    delivered = list_order.filter(status = 'Delivered').count()
    pending = list_order.filter(status = 'Pending').count()
    context = {
        'judul': 'halaman beranda',
        'menu': 'home',
        'custumer' :list_custumer,
        'order' :list_order,
        'data_total_orders':total_order,
        'delivered':delivered,
        'pending':pending,
    }
    return render(request, 'data/dashboard.html', context)

def products(request):
    list_product = Product.objects.all()

    context = {
        'judul': 'halaman product',
        'menu': 'products',    
        'product':list_product,
    }
    return render(request, 'data/product.html', context)

def custumer(request, hqq):
    detailcustumer = Custumer.objects.get(id=hqq)
    ordercustumer = detailcustumer.order_set.all()
    total_custumer = ordercustumer.count()
    context = {
        'judul': 'halaman custumer',
        'custumer': detailcustumer,
        'data_order_custumer': ordercustumer,
        'data_total' : total_custumer,
    }
    return render(request, 'data/custumer.html', context)

def createOrder(request,):
    formorder = OrderFrom()
    if request.method == 'POST':
        # print('cetak POST:',request.POST)
        formsimpan = OrderFrom(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
        
    context = {
        'judul': 'form order',
        'form' : formorder,
    }
    return render(request, "data/order_form.html", context)  

def updateOrder(request, lpp):
    orderupdate = Order.objects.get(id=lpp)
    formorder = OrderFrom(instance=orderupdate)
    if request.method == 'POST':
        # print('cetak POST:',request.POST)
        formedit = OrderFrom(request.POST, instance=orderupdate)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')
        
    context = {
        'judul':'Edit Order',
        'form' : formorder,
    }
    return render(request, "data/order_form.html", context) 

def deleteOrder(request, anj):
    Orderhapus = Order.objects.get(id=anj)
    if request.method == 'POST':
        Orderhapus.delete()
        return redirect('/')
    
    context = {
        'judul':'Hapus data Order',
        'dataorderhapus':Orderhapus,
    }
    return render(request, "data/delete_form.html", context)

def createcustumer(request,):
    formcstmr = CustumerForm()
    if request.method == 'POST':
        # print('cetak POST:',request.POST)
        formsimpan = CustumerForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
        
    context = {
        'judul': 'form order',
        'formc' : formcstmr,
    }
    return render(request, "data/custumer_form.html", context)  

def updateCustumer(request, apa):
    custumerupdate = Custumer.objects.get(id=apa)
    formcustumer = CustumerForm(instance=custumerupdate)
    if request.method == 'POST':
        # print('cetak POST:',request.POST)
        custumeredit = CustumerForm(request.POST, instance=custumerupdate)
        if custumeredit.is_valid:
            custumeredit.save()
            return redirect('/')
        
    context = {
        'judul':'Edit Custumer',
        'edit' : formcustumer,
    }
    return render(request, "data/update_custumer.html", context) 

def deleteCustumer(request, apb):
    Custumerhapus = Custumer.objects.get(id=apb)
    if request.method == 'POST':
        Custumerhapus.delete()
        return redirect('/')
    
    context = {
        'judul': 'hapus custumer',
        'deletecustumer': Custumerhapus,
    }
    return render(request, "data/delete_custumer.html", context)

def order(request, ye):
    detailorder = Order.objects.get(id=ye)
    li_order = detailorder.order_set.all()
    context = {
        'judul': 'halaman custumer',
        'custumer': detailorder,
        'data_order_custumer': li_order ,
    }
    return render(request, 'data/order.html', context)