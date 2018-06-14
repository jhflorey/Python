from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'session_words/index.html')

def delete(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/session_words')
    

def create(request):
    new_word = {}
    if request.method =='POST':
        print(request.POST)
        for key, value in request.POST.items():
            if key != "csrfmiddlewaretoken"  and key != "show_big":
                new_word[key] = value
            if key== "show_big":
                new_word["big"] = "big"
            else:
                new_word["big"] = ""
        created_at = datetime.now().strftime("%-H:%M:%S %p, %B %-d %Y")
        print(created_at)
        new_word['created_at'] = created_at
        if len(new_word['content']) > 50:
            new_word['content'] = new_word['content'][:50]
            
        if 'data' not  in request.session:
            request.session['data'] =[new_word,]
        else:
            temp_list = request.session['data']
            temp_list.append(new_word)
            request.session['data'] =temp_list
            
    return redirect('/session_words/')

