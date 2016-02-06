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
        unis = University.objects.all()
        result = []
        if (query[0] == "consent"):
            for i in range(0, len(unis)):
                if unis[i].consent == True:
                    result.append(unis[i])

        if (query[0] == "sexual assault"):
            for i in range(0, len(unis)):
                if unis[i].sexualassault == True:
                    result.append(unis[i])

        if (query[0] == "primary prevention"):
            for i in range(0, len(unis)):
                if unis[i].primaryprevention == True:
                    result.append(unis[i])
        
        context["universities"] = result
        context["q"] = query
        context["query0"] = query[0]
        return render(request, 'search-results.html', context)


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
