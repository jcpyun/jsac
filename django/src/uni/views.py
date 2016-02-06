from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext

from django.contrib.auth.models import User
from .models import *
from .forms import *
import datetime
# Create your views here.
def home(request):
    template= "home.html"
    # form = userForm(request.POST or None)
    # form = userForm(request.POST or None)
    # if request.method == "POST":
    #     print request.POST
    #   # instance = form.save(commit=False)
    
    ######## FORMS ######
    form = University(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
      
        instance.save()
    
    # form2 = Information(request.POST or None)
    # if form2.is_valid():
    #     instance2= form2.save(commit=False)
    #     print "test", instance2, "formwfoianweofainwer"
    #     instance2.save()
    # form3 = Teach(request.POST or None)
    # if form3.is_valid():
    #     instance3= form3.save(commit=False)
    #     print "test", instance3, "formwfoianweofainwer"
    #     instance3.save()
    # form4 = WeOffer(request.POST or None)
    # if form4.is_valid():
    #     instance4= form4.save(commit=False)
    #     print "test", instance4, "formwfoianweofainwer"
    #     instance4.save()
    ##### FORMS #####
    current_user = request.user    #this displays current user
    #####
    context={
        "form": form,

        "current_user": current_user,
        
       
        
    }
    
    return render(request,template,context)

