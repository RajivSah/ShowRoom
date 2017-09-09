from django import forms
from .models import part_stock, applicable_model,part_processing


class part_add_form(forms.Form):
    part_id=forms.CharField(max_length=30)
    part_name=forms.CharField(max_length=30)
    cost=forms.IntegerField(required=False)

class part_stock_form(forms.ModelForm):
    class Meta:
        model = part_stock
        fields = '__all__'

class applicable_form(forms.ModelForm):
    class Meta:
        model = applicable_model
        fields = '__all__'

class part_processing_form(forms.ModelForm):
    class Meta:
        model = part_processing
        fields = '__all__'

