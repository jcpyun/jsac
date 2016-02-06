from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext

from django.contrib.auth.models import User
from .models import *
from .forms import userForm
import datetime
# Create your views here.
def home(request):
    template= "home.html"
    # form = userForm(request.POST or None)
    # form = userForm(request.POST or None)
    # if request.method == "POST":
    #     print request.POST
	# 	# instance = form.save(commit=False)
    
    ######## FORMS ######
    form = userForm(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
        print instance, "WOWOWOOWOWOW"
        instance.save()
    ##### FORMS #####
    current_user = request.user    #this displays current user
    #####
    queryset=University.objects.all()####### 
    checkmark=queryset[0].checktest
    
    
    context={
        "current_user": current_user,
        "form": form,
        "university": queryset,
        "checkmark": checkmark,
    }
    return render(request,template,context)

