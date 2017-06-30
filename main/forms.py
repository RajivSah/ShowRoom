from django import forms
from main.models import employee

class login_form(forms.Form):
	username = forms.CharField(max_length=30,label='Username')
	password = forms.CharField(widget=forms.PasswordInput())

class employee_form(forms.ModelForm):
	class Meta:
		model=employee
		fields=['first_name','last_name','Gender','department_id','address_city','address_city', 'address_district', 'contact', 'salary', 'joined_date']
