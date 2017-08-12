from django import forms
from .models import Sales



class SalesForm(forms.ModelForm):
    class Meta:
        model=Sales
        fields='__all__'

