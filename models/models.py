import datetime

from django.db import models
from customer.models import customer_info
class model_first(models.Model):
    manufacturer = models.CharField(max_length=30)
    product_name = models.CharField(max_length=60,unique=True)

    def __str__(self):
        return self.product_name

class model_last(models.Model):
    modelFirst = models.ForeignKey(model_first,on_delete=models.CASCADE)
    model_last_name = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    available_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.model_last_name

class customer_vehicle_info(models.Model):
    customerId = models.ForeignKey(customer_info,on_delete=models.CASCADE)
    model_lastId = models.ForeignKey(model_last,on_delete=models.CASCADE)
    VRN = models.CharField(max_length=20)
    VIN = models.CharField(max_length=40)

    def __str__(self):
        return str(self.customerId)+"-"+str(self.model_lastId)

class model_stock(models.Model):
    modelLastId = models.ForeignKey(model_last,on_delete=models.CASCADE)
    entry_date = models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    amount = models.IntegerField(default=0)
    mfg_year = models.IntegerField(default=0)

    def __str__(self):
        return str(self.entry_date)