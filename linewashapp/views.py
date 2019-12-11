import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView


# Create your views here.

def home(request):
   return render(request, "home.html", {})


def health(request):
    return HttpResponse(PageView.objects.count())
