from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    all_products = []
    catprods = Product.objects.values('Sub_Category','id')
    cats = {item['Sub_Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Sub_Category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([prod,range(1,nslides),nslides])


    params = {'all_products':all_products}
    return render(request,'Kcart/HomePage.html',params)
def searchMatch(query,item):
    if query in item.Description.lower() or query in item.Product_Name.lower() or query in item.Category.lower():

        return True
    else:
        return False
def Search(request):
    query = request.GET.get('search')
    all_products = []
    catprods = Product.objects.values('Sub_Category','id')
    cats = {item['Sub_Category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(Sub_Category=cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]

        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            all_products.append([prod,range(1,nslides),nslides])

    params = {'all_products':all_products,'msg':''}
    if len(all_products)== 0 or len(query)<4:
        params = {'msg':'Product not found.Make sure to enter correct name of product.'}

    return render(request,'Kcart/search.html',params)


def Login(request):
    all_products = []
    catprods = Product.objects.values('Sub_Category','id')
    cats = {item['Sub_Category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(Sub_Category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([prod,range(1,nslides),nslides])


    params = {'all_products':all_products}
    return render(request,'Kcart/home2.html',params)
def Register(request):
    number = 10
    params={'n':number}
    return render(request,'Kcart/Home3.html',params)
def About(request):
    return render(request,'Kcart/about.html')
def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name','')
        phone=request.POST.get('phone','')
        email = request.POST.get('email','')
        desc= request.POST.get('desc','')
        con = Contact(Name=name,Email=email,Phone=phone,Description=desc)
        con.save()

    return render(request,'Kcart/contact.html')

def Cart(request):
    return render(request,'Kcart/cart.html')
def CheckOut(request):
    if request.method == "POST":
        items_json =request.POST.get('itemJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + "," + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        additional_phone = request.POST.get('additional_phone', '')
        ord = Orders(items_json=items_json ,name=name,amount = amount, email=email, phone=phone,address=address, city=city, state=state, zip_code =zip_code,additional_phone= additional_phone )
        ord.save()
        update = OrderUpdate(order_id = ord.order_id, update_desc = "ORDER HAS BEEN PLACED ")
        update.save()
        thank =True
        id = ord.order_id
        return render(request,'Kcart/checkout.html',{'thank': thank, 'id':id})
    return render(request,'Kcart/checkout.html')

def ProductView(request,myid):
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request,'Kcart/productview.html',{'product':product[0]})
def Success(request):
    return render(request, 'Kcart/sucess.html')
def Tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email','')
        try:
            order =Orders.objects.filter(order_id = orderId,email = email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id =orderId)
                updates =[]
                for i in update:
                    updates.append({'text':i.update_desc,'time': i.timestamp})
                    response = json.dumps({"status":"success" ,'updates':updates,'itemsJson':order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"success":"success"}')
        except Exception as e:
            return HttpResponse("{'success':'error'}")
    return render(request, 'Kcart/tracker.html')