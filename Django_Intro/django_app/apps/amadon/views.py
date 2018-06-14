from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
PRODUCT = [{'name':'Dojo Tshirt',
            'price': 19.99,
            'id':1},
           {'name':'Dojo Sw',
           'price': 29.99,
           'id':2},
           {'name':'Dojo Skirt',
            'price': 39.99,
            'id':3},
           {'name':'Dojo Pant',
           'price': 49.99,
           'id':4}]

# Create your views here.

def index(request):
    content = {'items':PRODUCT}
    return render(request, 'amadon/index.html', content)

def clear(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect(reverse('index'))

def process(request, item_id):
    for item in PRODUCT:
        print(item['id'])
        if item['id']==int(item_id):
            price = item['price']
            name = item['name']
            break
    quantity = int(request.POST['quantity'])
    request.session['price'] = price
    request.session['name'] = name
    request.session['quantity'] = quantity
    request.session['cost'] = round(price*quantity,2)
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
    if 'total_cost' not in request.session:
        request.session['total_cost'] = 0
    request.session['total_quantity'] += request.session['quantity']
    request.session['total_cost'] += request.session['cost']
    return redirect(reverse('checkout'))

def checkout(request):
    return render(request, 'amadon/checkout.html')

