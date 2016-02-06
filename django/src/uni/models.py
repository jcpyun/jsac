from __future__ import unicode_literals

from django.db import models

class WeOffer(models.Model):
    riskreduction = models.BooleanField(default=False)
    riskreductionDesc = models.TextField()
    primaryprevention = models.BooleanField(default=False)
    primarypreventionDesc = models.TextField()
    primarypreventionfresh = models.BooleanField(default=False)
    primarypreventionfreshonline = models.BooleanField(default=False)
    primarypreventionfreshinperson = models.BooleanField(default=False)
    primarypreventionfreshnumhours = models.IntegerField()
    primarypreventionfreshofftheshelf = models.BooleanField(default=False)
    primarypreventionfreshofftheshelfDesc = models.CharField(max_length=80)
    primarypreventionupper = models.BooleanField(default=False)
    primarypreventionupperonline = models.BooleanField(default=False)
    primarypreventionupperinperson = models.BooleanField(default=False)
    primarypreventionuppernumhours = models.IntegerField()
    primarypreventionupperofftheshelf = models.BooleanField(default=False)
    primarypreventionupperofftheshelfDesc = models.CharField(max_length=80)
    primarypreventiongrad = models.BooleanField(default=False)
    primarypreventiongradonline = models.BooleanField(default=False)
    primarypreventiongradinperson = models.BooleanField(default=False)
    primarypreventiongradnumhours = models.IntegerField()
    primarypreventiongradofftheshelf = models.BooleanField(default=False)
    primarypreventiongradofftheshelfDesc = models.CharField(max_length=80)
    facultystafftraining = models.BooleanField(default=False)
    facultystafftrainingDesc = models.CharField(max_length=80)
    facultystafftrainingrepeated = models.BooleanField(default=False)
    facultystafftrainingrepeatedFrequency = models.IntegerField() # Number of Frequency
    facultystafftrainingrepeatedFrequencyType = models.IntegerField() # 1=Week, 2=Month, 3=Year
    facultystafftrainingonline = models.BooleanField(default=False)
    facultystafftraininginperson = models.BooleanField(default=False)

class Groups(models.Model):
    titleixoffice = models.BooleanField(default=False)
    titleixofficeDesc = models.TextField()
    volunteergroup = models.BooleanField(default=False)
    volunteergroupDesc = models.TextField()
    studentinitiative = models.BooleanField(default=False)
    studentinitiativeDesc = models.TextField()
    mensgroup = models.BooleanField(default=False)
    mensgroupDesc = models.TextField()
    otheroffices = models.BooleanField(default=False)
    otherofficesDesc = models.TextField()

class Stats(models.Model):
    oncampusreports = models.BooleanField(default=False)
    oncampusreportsDesc = models.TextField()
    allreports = models.BooleanField(default=False)
    allreportsDesc = models.TextField()
    climatestudy = models.BooleanField(default=False)
    climatestudyDesc = models.TextField()

class Teach(models.Model):
    consent = models.BooleanField(default=False)
    consentDesc = models.TextField()
    sexualassault = models.BooleanField(default=False)
    sexualassaultDesc = models.TextField()
    sexualharassment = models.BooleanField(default=False)
    sexualharassmentDesc = models.TextField()
    stalking = models.BooleanField(default=False)
    stalkingDesc = models.TextField()
    datingviolence = models.BooleanField(default=False)
    datingviolenceDesc = models.TextField()
    domesticviolence = models.BooleanField(default=False)
    domesticviolenceDesc = models.TextField()

class Information(models.Model):
    aboutpolicies = models.BooleanField(default=False)
    aboutpoliciesDesc = models.TextField()
    aboutreporting = models.BooleanField(default=False)
    aboutreportingDesc = models.TextField()
    aboutreportingonline = models.BooleanField(default=False)

class Policy(models.Model):
    weoffer = WeOffer()
    groups = Groups()
    stats = Stats()
    teach = Teach()
    information = Information()

class University(models.Model):
    college = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    population = models.CharField(max_length=80)
    checktest = models.BooleanField(default=False)
    policy = Policy()

    def __unicode__(self):
        return self.college
