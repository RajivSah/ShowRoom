from django.http import HttpResponse
from .models import job_records

def index( request ):
    all_records = job_records.objects.all()
    html=''
    for i in all_records:
        url ='/workshop/' + str(i) + '/ '
        html += '<a href = "'+ url +'">'+ str(i.vid) +'</a><br>'
    return HttpResponse( html )

#def add_record()