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
        if not query: query = ""
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

class CreateUniv(View):
    def post(self, request):
        data = request.POST
        university_data = UniversityData.objects.get(id=data.get("uni_id")) #here, we'd get the current session's university
        instance = University(college=university_data)
        instance.save()
        instance.riskreduction = bool(data.get('policies-riskreductiondesc'))
        instance.riskreductionDesc = data.get('policies-riskreductiondesc')
        instance.primaryprevention = bool(data.get('policies-primarypreventiondesc'))
        instance.primarypreventionDesc = data.get('policies-primarypreventiondesc')
        instance.facultystafftraining = bool(data.get('policies-facultystafftrainingdesc'))
        instance.facultystafftrainingDesc = data.get('policies-facultystafftrainingdesc')

        instance.titleixoffice = bool(data.get('groups-titleixofficedesc'))
        instance.titleixofficeDesc = data.get('groups-titleixofficedesc')
        instance.volunteergroup = bool(data.get('groups-volunteergroupdesc'))
        instance.volunteergroupDesc = data.get('groups-volunteergroupdesc')
        instance.studentinitiative = bool(data.get('groups-studentinitiativedesc'))
        instance.studentinitiativeDesc = data.get('groups-studentinitiativedesc')
        instance.mensgroup = bool(data.get('groups-mensgroupdesc'))
        instance.mensgroupDesc = data.get('groups-mensgroupdesc')
        instance.otheroffices = bool(data.get('groups-otherofficesdesc'))
        instance.otherofficesDesc = data.get('groups-otherofficesdesc')

        instance.oncampusreports = bool(data.get('stats-oncampusreportsdesc'))
        instance.oncampusreportsDesc = data.get('stats-oncampusreportsdesc')
        instance.allreports = bool(data.get('stats-allreportsdesc'))
        instance.allreportsDesc = data.get('stats-allreportsdesc')
        instance.climatestudy = bool(data.get('stats-climatestudydesc'))
        instance.climatestudyDesc = data.get('stats-climatestudydesc')

        instance.consent = bool(data.get('training-consentdesc'))
        instance.consentDesc = data.get('training-consentdesc')
        instance.sexualassault = bool(data.get('training-sexualassaultdesc'))
        instance.sexualassaultDesc = data.get('training-sexualassaultdesc')
        instance.sexualharassment = bool(data.get('training-sexualharassmentdesc'))
        instance.sexualharassmentDesc = data.get('training-sexualharassmentdesc')
        instance.stalking = bool(data.get('training-stalkingdesc'))
        instance.stalkingDesc = data.get('training-stalkingdesc')
        instance.datingviolence = bool(data.get('training-datingviolencedesc'))
        instance.datingviolenceDesc = data.get('training-datingviolencedesc')
        instance.domesticviolence = bool(data.get('training-domesticviolencedesc'))
        instance.domesticviolenceDesc = data.get('training-domesticviolencedesc')

        instance.aboutpolicies = bool(data.get('awareness-aboutpoliciesdesc'))
        instance.aboutpoliciesDesc = data.get('awareness-aboutpoliciesdesc')
        instance.aboutpoliciesonline = data.get('awareness-aboutpoliciesonline')
        instance.aboutreporting = bool(data.get('awareness-aboutreportingdesc'))
        instance.aboutreportingDesc = data.get('awareness-aboutreportingdesc')
        instance.aboutreportingonline = data.get('awareness-aboutreportingonline')

        instance.save()
        return HttpResponseRedirect('/')

    def __str__(self):
        return self.college

class BuildProfile(View):
    def get(self, request):
        return render(request, 'build-profile.html')
    def post(self, request):
        data = request.POST
        instance = UniversityData()
        instance.name = data.get('university')
        instance.logo = data.get('logo')
        instance.coordinator = data.get('coordinator')
        instance.coordinator_email = data.get('email')
        instance.save()
        return HttpResponseRedirect('/policyform/%d' % instance.id)

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
    def get(self, request, uni_id):
        context = {}
        context["uni_id"] = uni_id
        return render(request, 'policy_form.html', context)


