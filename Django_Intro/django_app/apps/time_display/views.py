from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def index(request):
    date_time = strftime("%b %d, %Y - %H:%M %p")
    date, time = date_time.split('-')
    context = {"date": date, "time":time}
    return render(request, 'time_display/index.html',context )


#from django.shortcuts import render
#from time import gmtime, strftime
#def index(request):
 #   context = {"time": strftime("%Y-%m-%d $H:%M %p", gmtime())}
  #  return render(request, 'time_display/index.html', context)