from .models import customer_info
from django import forms
class cstm_add_form(forms.ModelForm):
    class Meta:
        model = customer_info
        fields = '__all__'