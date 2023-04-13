from django import forms
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm, PropertyForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Property
from django.views.generic import ListView, DetailView, CreateView, DeleteView

def home(request):
    template = loader.get_template('main/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/signup-success/')
    else:
        form = NewUserForm()
    return render(request, 'main/signup.html', {'register_form': form})

# def signup(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("/signup-success/")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="main/signup.html", context={"register_form":form})

def signup_success(request):
	template = loader.get_template('main/signup-success.html')
	context = {}
	return HttpResponse(template.render(context, request))

def signin(request):
    if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/signup-success/')
    else:
        form = NewUserForm()
    return render(request, 'main/signin.html', {'register_form': form})

def profile(request):
    template = loader.get_template('main/profile.html')
    context = {}
    return HttpResponse(template.render(context, request))

def checklist_filled(request):
    template = loader.get_template('main/checklist-filled.html')
    context = {}
    return HttpResponse(template.render(context, request))        

def checklists(request):
    template = loader.get_template('main/checklist.html')
    context = {}
    return HttpResponse(template.render(context, request))

def safety_portal(request):
	template = loader.get_template('main/safety-portal.html')
	context = {}
	return HttpResponse(template.render(context, request))
class PropertyCreateView(CreateView):
    form_class = PropertyForm
    template_name = 'main/property_form.html'
    success_url = 'checklist'

    def form_invalid(self, form):
        print(form.errors.as_data())
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
