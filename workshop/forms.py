from django import forms
from .models import job_records

class jobrecord_form(forms.ModelForm):
    class Meta:
        model = job_records
        fields = '__all__'