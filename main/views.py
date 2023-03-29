from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    template = loader.get_template('main/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/signup-success/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/signup.html", context={"register_form":form})

def signup_success(request):
	template = loader.get_template('main/signup-success.html')
	context = {}
	return HttpResponse(template.render(context, request)
		     )
def checklist(request):
    template = loader.get_template('main/checklist.html')
    context = {}
    return HttpResponse(template.render(context, request))