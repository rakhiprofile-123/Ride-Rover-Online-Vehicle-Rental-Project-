from django.shortcuts import render,redirect
from user.models import*
from django.views.decorators.cache import cache_control
from django.core.files.storage import FileSystemStorage
# Create your views here.
def clientdash(request):
    return render(request,'clienthome.html')

def clientlogout(request):
    try:
        if request.session['student']!=None:
            del request.session['student']
            return redirect('signin')
    except:
        return redirect('signin')