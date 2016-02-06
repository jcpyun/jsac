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

class CreateUniv(View):
    def post(self, request):
        data = request.POST
        instance = University() #here, we'd get the current session's university
        instance.riskreduction = data.get('policies-riskreduction')
        instance.riskreductionDesc = data.get('policies-riskreductiondesc')
        instance.primaryprevention = data.get('policies-primaryprevention')
        instance.primarypreventionDesc = data.get('policies-primarypreventiondesc')
        instance.facultystafftraining = data.get('policies-facultystafftraining')
        instance.facultystafftrainingDesc = data.get('policies-facultystafftrainingdesc')

        instance.titleixoffice = data.get('groups-titleixoffice')
        instance.titleixofficeDesc = data.get('groups-titleixofficedesc')
        instance.volunteergroup = data.get('groups-volunteergroup')
        instance.volunteergroupDesc = data.get('groups-volunteergroupdesc')
        instance.studentinitiative = data.get('groups-studentinitiative')
        instance.studentinitiativeDesc = data.get('groups-studentinitiativedesc')
        instance.mensgroup = data.get('groups-mensgroup')
        instance.mensgroupDesc = data.get('groups-mensgroupdesc')
        instance.otheroffices = data.get('groups-otheroffices')
        instance.otherofficesDesc = data.get('groups-otherofficesdesc')

        instance.oncampusreports = data.get('stats-oncampusreports')
        instance.oncampusreportsDesc = data.get('stats-oncampusreportsdesc')
        instance.allreports = data.get('stats-allreports')
        instance.allreportsDesc = data.get('stats-allreportsdesc')
        instance.climatestudy = data.get('stats-climatestudy')
        instance.climatestudyDesc = data.get('stats-climatestudydesc')

        instance.consent = data.get('training-consent')
        instance.consentDesc = data.get('training-consentdesc')
        instance.sexualassault = data.get('training-sexualassault')
        instance.sexualassaultDesc = data.get('training-sexualassaultdesc')
        instance.sexualharassment = data.get('training-sexualharassment')
        instance.sexualharassmentDesc = data.get('training-sexualharassmentdesc')
        instance.stalking = data.get('training-stalking')
        instance.stalkingDesc = data.get('training-stalkingdesc')
        instance.datingviolence = data.get('training-datingviolence')
        instance.datingviolenceDesc = data.get('training-datingviolencedesc')
        instance.domesticviolence = data.get('training-domesticviolence')
        instance.domesticviolenceDesc = data.get('training-domesticviolencedesc')

        instance.aboutpolicies = data.get('awareness-aboutpolicies')
        instance.aboutpoliciesDesc = data.get('awareness-aboutpoliciesdesc')
        instance.aboutpoliciesonline = data.get('awareness-aboutpoliciesonline')
        instance.aboutreporting = data.get('awareness-aboutreporting')
        instance.aboutreportingDesc = data.get('awareness-aboutreportingdesc')
        instance.aboutreportingonline = data.get('awareness-aboutreportingonline')

        instance.save()
        return redirect('/university_page/')

class BuildProfile(View):
    def get(request):
        return render(request, 'build-profile.html')
    def post(request):
        data = request.POST
        instance = University()
        instance.college = data.get('college')
        instance.logo = data.get('logo')
        instance.save()
        return redirect('/form-information/')

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
    data_dump=[]
    for x in alluni:
        if x.college=="CMU":
            data_dump=x

    context={
        "data": data_dump,
        "pitt": "https://upload.wikimedia.org/wikipedia/commons/5/57/PittPanthers.png",
        "columbia": "http://vignette2.wikia.nocookie.net/nba/images/c/c7/Columbia_University.png/revision/latest?cb=20110506170850",
    }
    return render(request,template,context)

class PolicyForm(View):
    def get(self, request):
        return render(request, 'policy_form.html')
