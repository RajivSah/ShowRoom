from django import forms
from .models import *


class model_last_form(forms.ModelForm):
    class Meta:
        model = model_last
        fields = '__all__'


class model_stock_form(forms.ModelForm):
    class Meta:
        model = model_stock
        fields = '__all__'


class ManufacturerForm(forms.ModelForm):
        class Meta:
            model=Manufacturer
            fields='__all__'


class CategoryForm(forms.ModelForm):
        class Meta:
            model=VehicleCategory
            fields='__all__'


class VehicleNameForm(forms.ModelForm):
    class Meta:
        model = VehicleName
        fields = '__all__'


class ModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModels
        fields = '__all__'


class ModelDetailsForm(forms.ModelForm):
    class Meta:
        model = ModelDetails
        fields = '__all__'


class ImportDetailsForm(forms.ModelForm):
    class Meta:
        model = ImportDetails
        fields = '__all__'

