from django.http import HttpResponse, HttpResponseRedirect
from books.models import Book
from django.shortcuts import render

def search_req(request):
	
	lat_books=Book.objects.order_by('-date_added')[:5]
	if 'q' in request.GET and request.GET['q']:
		q=request.GET['q']
		books=Book.objects.filter(title__icontains=q)
		if books:
			dict={'books':books, 'query':q}
			return render(request, "search_res.html", dict);
		else:
			message={'error':True, 'message':'No Books matched your search criteria.','lat_books':lat_books}
			return render(request, "index.html", message);
		
	else:
		
		message={'error':True, 'message':'You have searced for empty value.','lat_books':lat_books}
		return render(request, "index.html", message);
	
	
