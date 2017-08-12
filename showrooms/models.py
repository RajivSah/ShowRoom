from django.db import models
from customer.models import customer_info
from vehicle_models.models import VehicleModels
import datetime




class Sales(models.Model):
    customer=models.ForeignKey(customer_info)
    model=models.ForeignKey(VehicleModels)
    VIN=models.CharField(max_length=30)
    VRN=models.CharField(max_length=30)
    dateOfSale=models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    soldRate=models.IntegerField(default=0)