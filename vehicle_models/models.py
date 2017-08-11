import datetime

from django.db import models
from customer.models import customer_info


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.manufacturer



class VehicleCategory(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category


class VehicleName(models.Model):
    category = models.ForeignKey(VehicleCategory, on_delete=models.CASCADE)
    vehicleName = models.CharField(max_length=30)
    image=models.ImageField(upload_to='media',blank=True,null=True,)
    def __str__(self):
        return self.vehicleName


class VehicleModels(models.Model):
    vehicleName=models.ForeignKey(VehicleName,on_delete=models.CASCADE)
    model=models.CharField(max_length=30)
    def __str__(self):
        return self.model


class ModelDetails(models.Model):
    model=models.ForeignKey(VehicleModels,on_delete=models.CASCADE)
    specs=models.CharField(max_length=1000)
    availableQty=models.IntegerField(default=0)



class ImportDetails(models.Model):
    model=models.ForeignKey(VehicleModels,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)
    importDate=models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))

class ModelStock(models.Model):
    model=models.ForeignKey(VehicleModels,on_delete=models.CASCADE)
    color=models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)


class model_first(models.Model):
    manufacturer = models.CharField(max_length=30)
    product_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.product_name


class model_last(models.Model):
    modelFirst = models.ForeignKey(model_first, on_delete=models.CASCADE)
    model_last_name = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    available_qty = models.IntegerField(default=0)

    def __str__(self):
        return self.model_last_name


class customer_vehicle_info(models.Model):
    customerId = models.ForeignKey(customer_info, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModels, on_delete=models.CASCADE)
    VRN = models.CharField(max_length=20)
    VIN = models.CharField(max_length=40)

    def __str__(self):
        return self.VRN

class model_stock(models.Model):
    modelLastId = models.ForeignKey(model_last, on_delete=models.CASCADE)
    entry_date = models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    amount = models.IntegerField(default=0)
    mfg_year = models.IntegerField(default=0)

    def __str__(self):
        return str(self.entry_date)
