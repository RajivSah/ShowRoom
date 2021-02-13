from django.db import models
from customer.models import customer_info
from vehicle_models.models import VehicleModels,ModelStock
import datetime




class Sales(models.Model):
    customer=models.ForeignKey(customer_info,on_delete=models.CASCADE)
    model=models.ForeignKey(ModelStock,on_delete=models.CASCADE)

    VIN=models.CharField(max_length=30)
    VRN=models.CharField(max_length=30)
    dateOfSale=models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    soldRate=models.IntegerField(default=0)
