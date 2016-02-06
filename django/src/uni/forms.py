from django import forms
from django.forms import ModelForm
from .models import *

from .models import *



class University(ModelForm):
    class Meta:
        model= University
        exclude=['']


# class ArticleForm(ModelForm):
# ...     class Meta:
# ...         model = Article
# ...         fields = ['pub_date', 'headline', 'content', 'reporter']

# class userForm(ModelForm):
#     field1 = forms.CharField()
#     field1 = forms.CharField()
#     bool1 = forms.BooleanField(required=False)
#     date1 = forms.DateField(required=False)