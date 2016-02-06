from django.shortcuts import render, get_object_or_404, render_to_response, RequestContext

from django.contrib.auth.models import User
from .models import *

import datetime
# Create your views here.
def home(request):
    template= "home.html"
    current_user = request.user
    context={
        "current_user": current_user,
    }
    return render(request,template,context)

