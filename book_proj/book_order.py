from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from books.models import Book
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

def add_cart(request):
	if request.method=='POST':
		print(request.POST['bid'])
		return redirect('/');
	else:
		return redirect('/');

