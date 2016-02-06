from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext

from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime
# Create your views here.
def home(request):
    template= "home.html"
    
    form = University(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
      
        instance.save()
    
  
    ##### FORMS #####
    current_user = request.user    #this displays current user
    #####
    context={
        "form": form,

        "current_user": current_user,
        
    }
    
    return render(request,template,context)

def create_uni(request):
    template="form.html"
    form = University(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
      
        instance.save()
    context={
        "form": form,

    }
    return render(request,template,context)