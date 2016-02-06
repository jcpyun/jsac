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

mapping = {
    "risk reduction": "riskreduction",
    "primary prevention": "primaryprevention",
    "faculty-staff training": "facultystafftraining",
    "title IX office": "titleixoffice",
    "volunteer group": "volunteergroup",
    "student initiative": "studentinitiative",
    "mens group": "mensgroup",
    "other offices": "otheroffices",
    "stats on campus reports": "oncampusreports",
    "stats on all reports": "allreports",
    "stats on climate studies": "climatestudy",
    "consent": "consent",
    "sexual assault": "sexualassault",
    "sexual harassment": "sexualharassment",
    "stalking": "stalking",
    "dating violence": "datingviolence",
    "domestic violence": "domesticviolence",
    "awareness about policies": "aboutpolicies",
    "awareness about reporting": "aboutreporting"
}

reverse_mapping = {mapping[key]: key for key in mapping}

def getMatchesOfFields(fields):
    forms = University.objects.all()
    unis = []
    for form in forms:
        for field in fields:
            if form.__getattribute__(field):
                unis.append(form)
                break
    return unis

class SearchPage(View):
    def get(self, request):
        context = {}
        query = request.GET.get("q")
        if not query: query = ""
        query = query.split(",")
        fields = []
        for q_word in query:
            fields.append(mapping[q_word])
        matches = getMatchesOfFields(fields)
        universities = []
        print matches
        for match in matches:
            for field in fields:
                data = {}
                data["university_name"] = match.college.name
                data["topic"] = reverse_mapping[field]
                data["description"] = match.__getattribute__(field + "Desc")
                data["university_pic"] = match.college.logo
                data["id"] = match.college.id
                universities.append(data)
        import random
        context["q"] = query
        context["universities"] = universities
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


def university_page(request, uni_id):
    template="university_page.html"
    university = UniversityData.objects.get(id=int(uni_id))
    form_data = university.form_data
    context = {}
    context["name"] = university.name
    context["picture"] = university.logo
    context["data"] = form_data
    return render(request,template,context)

class PolicyForm(View):
    def get(self, request, uni_id):
        context = {}
        context["uni_id"] = uni_id
        return render(request, 'policy_form.html', context)


