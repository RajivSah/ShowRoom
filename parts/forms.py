from django import forms
import datetime
import re

from django.core.exceptions import ValidationError


class part_add_form(forms.Form):
    part_id=forms.CharField(max_length=30)
    part_name=forms.CharField(max_length=30)
    cost=forms.IntegerField(required=False)

class part_stock_form(forms.Form):
    stock_id=forms.CharField(max_length=30,required=False)
    entry_date=forms.DateField(widget=forms.DateInput(),initial=datetime.date.today())
    supplier=forms.CharField(max_length=30)
    amount=forms.IntegerField()

class applicable_form(forms.Form):
    app_id=forms.CharField(max_length=30,required=False);
    applicable=forms.CharField(max_length=30)
