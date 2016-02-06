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
    
    form = university(request.POST or None)
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
        query = request.GET.get("q")
        query = query.split(",")
        context["universities"] = fakeResultsData
        context["q"] = query
        return render(request, 'search-results.html', context)


def create_uni(request):
    template="form.html"
    form = university(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
      
        instance.save()
    context={
        "form": form,

    }
    return render(request,template,context)

def university_page(request):
    template="university_page.html" 
    alluni= University.objects.all()
    data=[]
    for x in alluni:
        if x.college=="CMU":
            data_dump=x

    context={
        "data":data_dump,

    }
    return render(request,template,context)

class PolicyForm(View):
    def get(self, request):
        return render(request, 'policy_form.html')
