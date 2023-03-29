from django import forms
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Property
from django.views.generic import ListView, DetailView, CreateView, DeleteView

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
def checklists(request):
    template = loader.get_template('main/checklist.html')
    context = {}
    return HttpResponse(template.render(context, request))

class PropertyCreateView(CreateView):
	model = Property
	fields = ['name', 'type', 'address', 'notes', 'image', 'safety', 'convenience'] 

	def get_form(self, form_class=None):
			if form_class is None:
				form_class = self.get_form_class()

			form = super(PropertyCreateView, self).get_form(form_class)
			form.fields['name'].widget = forms.TextInput(attrs={'placeholder': 'Enter property name (e.g. Orchid Apartment)*'})
			form.fields['type'].widget = forms.TextInput(attrs={'placeholder': 'Enter property type (e.g. lowrise, midrise, highrise, 2-storeyhouse)'})
			form.fields['address'].widget = forms.TextInput(attrs={'placeholder': 'Enter address'})
			form.fields['notes'].widget = forms.TextInput(attrs={'placeholder': 'Enter other notes (as needed)'})
			return form
