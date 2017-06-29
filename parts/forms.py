from django import forms

class part_add_form(forms.Form):
    part_id=forms.CharField(max_length=30)
    part_name=forms.CharField(max_length=30)
    cost=forms.IntegerField(required=False)
