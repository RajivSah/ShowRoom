from django import forms

class ContactForm(forms.Form):
	subject=forms.CharField()
	email=forms.EmailField(required=False)
	message=forms.CharField()

class SearchBar(forms.Form):
	keyword=forms.CharFiels()
