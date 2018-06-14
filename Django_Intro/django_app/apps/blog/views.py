from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')
    #return HttpResponse('placeholder to later display all the list of blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    if request.method == "POST":
        print( "*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = request.POST['name']
        request.session['desc'] = request.POST['desc']
        request.session['counter'] = 100
        print("*"*50)
        return redirect("/blog")
    else:
        return redirect("/blog")
        

def show(request, number):
    return HttpResponse('placeholder to display blog %s'%(number))

def edit(request, number):
    content = {'number': number}
    return render(request, 'blog/edit.html', content)
    #return HttpResponse('placeholder to edit blog %s'%(number))

def destroy(request, number):
    return redirect('/blog')