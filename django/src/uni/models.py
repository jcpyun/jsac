from __future__ import unicode_literals

from django.db import models

class University(models.Model):
    college = models.CharField(max_length=80, default='')
    logo= models.TextField(blank=True)
    state = models.CharField(max_length=80, default='')
    city = models.CharField(max_length=80, default='')
    population = models.CharField(max_length=80, default='')
  
    #Awareness
    aboutpolicies = models.BooleanField(default=True)
    aboutpoliciesDesc = models.TextField(blank=True)
    aboutpoliciesonline = models.BooleanField(default=False)
    aboutreporting = models.BooleanField(default=False)
    aboutreportingDesc = models.TextField(blank=True)
    aboutreportingonline = models.BooleanField(default=False)

    #Training
    consent = models.BooleanField(default=False)
    consentDesc = models.TextField(blank=True)
    sexualassault = models.BooleanField(default=False)
    sexualassaultDesc = models.TextField(blank=True)
    sexualharassment = models.BooleanField(default=False)
    sexualharassmentDesc = models.TextField(blank=True)
    stalking = models.BooleanField(default=False)
    stalkingDesc = models.TextField(blank=True)
    datingviolence = models.BooleanField(default=False)
    datingviolenceDesc = models.TextField(blank=True)
    domesticviolence = models.BooleanField(default=False)
    domesticviolenceDesc = models.TextField(blank=True)
   
    #Statistics
    oncampusreports = models.BooleanField(default=False)
    oncampusreportsDesc = models.TextField(blank=True)
    allreports = models.BooleanField(default=False)
    allreportsDesc = models.TextField(blank=True)
    climatestudy = models.BooleanField(default=False)
    climatestudyDesc = models.TextField(blank=True)


    #Groups
    titleixoffice = models.BooleanField(default=False)
    titleixofficeDesc = models.TextField(blank=True)
    volunteergroup = models.BooleanField(default=False)
    volunteergroupDesc = models.TextField(blank=True)
    studentinitiative = models.BooleanField(default=False)
    studentinitiativeDesc = models.TextField(blank=True)
    mensgroup = models.BooleanField(default=False)
    mensgroupDesc = models.TextField(blank=True)
    otheroffices = models.BooleanField(default=False)
    otherofficesDesc = models.TextField(blank=True)


    #policies
    riskreduction = models.BooleanField(default=False)
    riskreductionDesc = models.TextField(blank=True)
    primaryprevention = models.BooleanField(default=False)
    primarypreventionDesc = models.TextField(blank=True)
    facultystafftraining = models.BooleanField(default=False)
    facultystafftrainingDesc = models.CharField(max_length=80, default='')


    def __unicode__(self):
        return self.college
