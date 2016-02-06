from __future__ import unicode_literals

from django.db import models

# Create your models here.
class university(models.Model):
    college=models.CharField(max_length=80)
    state=models.CharField(max_length=80)
    city=models.CharField(max_length=80)
    population=models.CharField(max_length=80)
    def __unicode__(self):
        return self.college
