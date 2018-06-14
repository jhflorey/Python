from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    
    return render(request, 'survey_form/index.html', )

def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if 'counter' not in request.session:
            request.session['counter'] =1
        else:
            request.session['counter'] +=1
        
        return redirect('/survey_form/result')
    else:
        return redirect('/survey_form')


def result(request):
    return render(request, 'survey_form/result.html')