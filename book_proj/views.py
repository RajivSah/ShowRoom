from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
class ContactForm(forms.Form):
	subject=forms.CharField()
	email=forms.EmailField(required=False)
	message=forms.CharField(widget=forms.Textarea)

def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			print('Hello World')
		return HttpResponseRedirect('/contact/thanks/')
	else:
		form=ContactForm()
		return render(request, 'contact_form.html', {'form':form})
