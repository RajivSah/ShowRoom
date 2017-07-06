from django import forms
import datetime
import re

from django.core.exceptions import ValidationError


class part_add_form(forms.Form):
    part_id=forms.CharField(max_length=30)
    part_name=forms.CharField(max_length=30)
    cost=forms.IntegerField(required=False)

class part_stock_form(forms.Form):
    entry_date=forms.DateField(widget=forms.DateInput(),initial=datetime.date.today())
    supplier=forms.CharField(max_length=30)
    amount=forms.IntegerField()

    # def clean(self):
    #     entry_date=self.cleaned_data['entry_date']
    #     print(entry_date)
        # if not re.match(r'(\d{4})[/.-](\d{2})[/.-](\d{2})$', str(entry_date)):
        #     raise ValidationError("enter 10")
        # return entry_date
