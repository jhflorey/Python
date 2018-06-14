# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
# Create your views here.
def new(request):
    return render(request, 'main_app/new_user.html')

def create(request):
    if request.method == 'POST':
        input_user = request.POST
        User.objects.create(first_name=input_user['first_name'],
                            last_name= input_user['last_name'],
                            email = input_user['email'])
        return redirect('/')
    else:
        return redirect('/new')

def index(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'main_app/index.html', context)

def show(request, user_id):
    my_user = User.objects.get(id=user_id)
    return render(request, 'main_app/show_user.html', {'user':my_user})

def edit(request, user_id):
    my_user = User.objects.get(id=user_id)
    return render(request, 'main_app/edit_user.html', {'user':my_user})


def delete(request, user_id):
    my_user = User.objects.get(id=user_id)
    if my_user is not None:
        my_user.delete()
    return redirect('/')

def update(request, user_id):
    if request.method == "POST":
        my_user = User.objects.get(id=user_id)
        my_user.first_name = request.POST['first_name']
        my_user.last_name = request.POST['last_name']
        my_user.email = request.POST['email']
        my_user.save()
        return redirect('/')
        #return redirect('/%s/show' % user_id)