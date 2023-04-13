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

	

	def clean(self):
        # data from the form is fetched using super function
		
		super(PropertyForm, self).clean()
         
        # extract the username and text field from the data
        
		fields = ['price', 'building_age', 'buliding_codes', 'fault_line', 'retrofitted', 'foundation_issues',
	    'soil', 'building_height', 'building_insurance', 'disaster_history', 'fire_exits', 'gas_valve',
		'evacuation_zone', 'essential_institutions']
	
		# total_score = self.cleaned_data.get('total_score')
		# total_score = float(total_score)
		price = self.cleaned_data.get('price')
		# price = str(price)
		print(type(price))
		building_age = str(self.cleaned_data.get('buillding_age'))
		building_codes = str(self.cleaned_data.get('building_codes'))
		fault_line = str(self.cleaned_data.get('fault_line'))
		retrofitted = str(self.cleaned_data.get('retrofitted'))
		foundation_issues = str(self.cleaned_data.get('foundation_issues'))
		soil = str(self.cleaned_data.get('soil'))
		building_height = str(self.cleaned_data.get('building_height'))
		building_insurance = str(self.cleaned_data.get('building_insurance'))
		disaster_history = str(self.cleaned_data.get('disaster_history'))
		fire_exits = str(self.cleaned_data.get('fire_exits'))
		gas_valve = str(self.cleaned_data.get('gas_valve'))
		evacuation_zone = str(self.cleaned_data.get('evacuation_zone'))
		essential_institutions = str(self.cleaned_data.get('essential_institutions'))
			
        # conditions to be met for the username length
        # if len(username) < 5:
        #     self._errors['username'] = self.error_class([
        #         'Minimum 5 characters required'])
        # if len(text) <10:
        #     self._errors['text'] = self.error_class([
        #         'Post Should Contain a minimum of 10 characters'])
 
        # return any errors if found
		return self.cleaned_data