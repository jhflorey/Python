from django.shortcuts import render, HttpResponse, redirect
from random import randint
from time import gmtime, strftime

# Create your views here.

def index(request):
    if 'total'  not in request.session:
        request.session['total'] = 0
    return render(request, 'ninja_gold/index.html')

def process(request, my_type):
    my_gold = 0
    create_time = strftime("%Y/%b/%d %H:%M %p", gmtime())
    if my_type == 'farm':
        my_gold = randint(10,21)
    if my_type == 'cave':
        my_gold = randint(5,11)
    if my_type == 'house':
        my_gold = randint(2,6)
    if my_type == 'casino':
        my_gold = randint(-51,51)
    if my_gold >= 0:
        message = 'Earn %s golds from the %s! (%s)'%(my_gold, my_type, create_time)
        color = 'green'
    else:
        message = 'Enter %s and lost %s golds ... Ouch. (%s)' % ( my_type, my_gold, create_time)
        color = 'red'
    new_log = {'class':color,
               'message': message}
    request.session['total'] += my_gold
    if 'logs' not in request.session:
        request.session['logs'] = [new_log,]
    else:
        logs = request.session['logs']
        logs.append(new_log)
        request.session['logs'] = logs
    return redirect('/ninja_gold/')