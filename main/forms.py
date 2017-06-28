from django import forms

class login_form(forms.Form):
    username = forms.CharField(max_length=30,label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
