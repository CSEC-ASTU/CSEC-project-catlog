import re

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators

from .models import User


# function for validating an Email
def validate_email(email):
	"""
		pass the regular expression
		and the string into the fullmatch() method 
		and chackes whether it is valid email or not  
		then rises validationError if it not valid

	"""
	# regular expression for validating an Email
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
	if not re.fullmatch(regex, email):
		raise forms.ValidationError('Invalid email format')


# user Registration form
class UserRegistrationForm(forms.ModelForm):
	email = forms.EmailField(validators=[validate_email])
	password = forms.CharField(label='Password',  widget=forms.PasswordInput, validators = [validate_password]) 
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'phone_number', 'email')
	def clean(self):
		cleaned_data = super(UserRegistrationForm, self).clean()
		password = cleaned_data.get("password")
		password2 = cleaned_data.get("password2")
		if password != password2:
			self.add_error('password2', "Passwords does not match")



			
