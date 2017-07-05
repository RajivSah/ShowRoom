from django import forms
import  datetime
class part_add_form(forms.Form):
    part_id=forms.CharField(max_length=30)
    part_name=forms.CharField(max_length=30)
    cost=forms.IntegerField(required=False)

class part_stock_form(forms.Form):
    entry_date=forms.DateField(initial=datetime.date.today())
    supplier=forms.CharField(max_length=30)
    amount=forms.IntegerField()
