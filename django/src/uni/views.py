from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext
from django.views.generic.base import View
from django.http import HttpResponseRedirect
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

fakeResultsData = [
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
    {
        "university_name": "Carnegie Mellon University",
        "statistic": "arbitrary statistic",
        "university_pic": "http://www.cmu.edu/homeimages/CarnegieMellonUniversity_wordmark.gif",
        "description": "Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis Lorem ipsum dolor sit amet, consecture, adipscing ecit. Maunis"
    },
]

class SearchPage(View):
    def get(self, request):
        context = {}
        context["universities"] = fakeResultsData
        return render(request, 'search-results.html', context)


