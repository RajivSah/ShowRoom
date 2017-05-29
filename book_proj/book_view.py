from django.template.loader import get_template
from django.http import HttpResponse
from books.models import Book
from django.shortcuts import render

def bk_view(request):
	bk_isbn=request.GET['isbn']
	book=Book.objects.filter(ISBN=bk_isbn)
	if book:
		return render(request, "bk_view.html", {'bk':book,});
	else:
		t=get_template("search_template.html")
		html=t.render({'error':'True', 'message':'Invalid Book. Try again'})
		return HttpResponse(html);
