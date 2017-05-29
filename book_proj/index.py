from django.http import HttpResponse
from django.template.loader import get_template
from books.models import Book

def view(request):
	latbooks=Book.objects.order_by('-date_added')[:5]
	t=get_template('index.html')
	html=t.render({'lat_books':latbooks,})
	return HttpResponse(html)
