from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Property

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class PropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'placeholder':'Enter property name (e.g. Orchid Apartment)*'}),
			'type': forms.TextInput(attrs={'placeholder':'Enter property type (e.g. lowrise, midrise, highrise, 2-storeyhouse)'}),
			'address': forms.Textarea(attrs={'placeholder':'Enter address'}),
			'notes': forms.Textarea(attrs={'placeholder':'Enter other notes (as needed)'}),
			'price': forms.RadioSelect(attrs={'class': 'property-form-price-radio'}),
			'building_age': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'building_codes': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'fault_line': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'retrofitted': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'foundation_issues': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'soil': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'building_height': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'building_insurance': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'disaster_history': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'fire_exits': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'gas_valve': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'evacuation_zone': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'}),
			'essential_institutions': forms.RadioSelect(attrs={'class': 'property-form-safety-radio'})
		}

	# name = forms.CharField(max_length=255, 
	# 		widget=forms.TextInput(attrs={'placeholder':'Enter property name (e.g. Orchid Apartment)*'}))
	# type = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Enter property type (e.g. lowrise, midrise, highrise, 2-storeyhouse)'}))
	# address = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter address'}))
	# notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter other notes (as needed)'}))
	# image = forms.ImageField()

	# price_select = [
    #     (1, 'Within budget'),
    #     (0, 'Overbudget')
    # ]
	# price = forms.ChoiceField(widget=forms.RadioSelect, choices = price_select)

	# class Meta:
	# 	model = Property
	# 	fields = '__all__'
	# building_age = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# building_codes = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# fault_line = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# retrofitted = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# foundation_issues = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# soil = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# building_height = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# building_insurance = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# disaster_history = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# fire_exits = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# gas_valve = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# evacuation_zone = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# essential_institutions = models.DecimalField(default=0, decimal_places=1, max_digits=2)
	# total_score = models.DecimalField(default=0, decimal_places=2, max_digits=10)