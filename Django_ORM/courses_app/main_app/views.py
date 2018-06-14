from django.shortcuts import render, redirect

#import models
from .models import *

# Create your views here
def index(request):
    # get all courses
    courses = Course.objects.all()
    return render(request, 'main_app/index.html', {'courses': courses})

def create(request):
    if request.method =='POST':
        if Course.objects.validate(request.POST):
            Course.objects.create(name=request.POST['name'],
                                  desc= request.POST['desc'] )
            return redirect('/')
        else:
            return redirect('/')

def destroy(request, course_id ):
    course = Course.objects.get(id=course_id)
    return render(request, 'main_app/view_destroy.html', {'course': course})


def confirm_destroy(request,course_id):
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
    except Exception as e:
        print('This course is not in the system')

    return redirect('/')
