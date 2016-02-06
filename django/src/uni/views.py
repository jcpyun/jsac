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


