from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'string' not in request.session:
        request.session['string'] = ''

    return render(request, "random_word_generator/index.html")

def create(request):
    request.session['counter'] += 1
    random = get_random_string(length=14)
    request.session['string'] = random
    
    return redirect('/')

def delete(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/')