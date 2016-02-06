from __future__ import unicode_literals

from django.db import models

class UniversityData(models.Model):
    name = models.CharField(max_length=100, default='')
    logo = models.CharField(max_length=300, default='')
    coordinator = models.CharField(max_length=100, default='')
    coordinator_email = models.CharField(max_length=100, default='')

class University(models.Model):
    college = models.CharField(max_length=80, default='')
    logo= models.TextField(blank=True)
    state = models.CharField(max_length=80, default='')
    city = models.CharField(max_length=80, default='')
    population = models.CharField(max_length=80, default='')
  
    #Awareness
    aboutpolicies = models.NullBooleanField(default=True)
    aboutpoliciesDesc = models.TextField(blank=True)
    aboutpoliciesonline = models.NullBooleanField(default=False)
    aboutreporting = models.NullBooleanField(default=False)
    aboutreportingDesc = models.TextField(blank=True)
    aboutreportingonline = models.NullBooleanField(default=False)

    #Training
    consent = models.NullBooleanField(default=False)
    consentDesc = models.TextField(blank=True)
    sexualassault = models.NullBooleanField(default=False)
    sexualassaultDesc = models.TextField(blank=True)
    sexualharassment = models.NullBooleanField(default=False)
    sexualharassmentDesc = models.TextField(blank=True)
    stalking = models.NullBooleanField(default=False)
    stalkingDesc = models.TextField(blank=True)
    datingviolence = models.NullBooleanField(default=False)
    datingviolenceDesc = models.TextField(blank=True)
    domesticviolence = models.NullBooleanField(default=False)
    domesticviolenceDesc = models.TextField(blank=True)
   
    #Statistics
    oncampusreports = models.NullBooleanField(default=False)
    oncampusreportsDesc = models.TextField(blank=True)
    allreports = models.NullBooleanField(default=False)
    allreportsDesc = models.TextField(blank=True)
    climatestudy = models.NullBooleanField(default=False)
    climatestudyDesc = models.TextField(blank=True)


    #Groups
    titleixoffice = models.NullBooleanField(default=False)
    titleixofficeDesc = models.TextField(blank=True)
    volunteergroup = models.NullBooleanField(default=False)
    volunteergroupDesc = models.TextField(blank=True)
    studentinitiative = models.NullBooleanField(default=False)
    studentinitiativeDesc = models.TextField(blank=True)
    mensgroup = models.NullBooleanField(default=False)
    mensgroupDesc = models.TextField(blank=True)
    otheroffices = models.NullBooleanField(default=False)
    otherofficesDesc = models.TextField(blank=True)


    #policies
    riskreduction = models.NullBooleanField(default=False)
    riskreductionDesc = models.TextField(blank=True)
    primaryprevention = models.NullBooleanField(default=False)
    primarypreventionDesc = models.TextField(blank=True)
    facultystafftraining = models.NullBooleanField(default=False)
    facultystafftrainingDesc = models.CharField(max_length=80, default='')


    def __unicode__(self):
        return self.college
