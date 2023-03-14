from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('main/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def checklist(request):
    template = loader.get_template('main/checklist.html')
    context = {}
    return HttpResponse(template.render(context, request))