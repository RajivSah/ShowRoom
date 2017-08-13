from django import forms
from .models import Sales
from customer.models import customer_info
from vehicle_models.models import *


class SalesForm(forms.ModelForm):
    class Meta:
        model=Sales

        fields=('customer','model','VIN','VRN','dateOfSale','soldRate')


