from django import forms
from .models import *
class model_last_form(forms.ModelForm):
    class Meta:
        model = model_last
        fields = '__all__'