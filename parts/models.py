from django.db import models
import datetime
from vehicle_models.models import customer_vehicle_info

class part_list(models.Model):
    part_id=models.CharField(max_length=30,unique=True)
    part_name=models.CharField(max_length=30)
    cost=models.IntegerField(default=0)
    available_quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.part_id

class applicable_model(models.Model):
    partId=models.ForeignKey(part_list, on_delete=models.CASCADE)
    applicable=models.CharField(max_length=30)

    def __str__(self):
        return self.partId

class part_stock(models.Model):
    part_id=models.ForeignKey(part_list,on_delete=models.CASCADE)
    entry_date=models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    supplier=models.CharField(max_length=30)
    amount=models.IntegerField(default=0)

    def __str__(self):
        return str(self.entry_date)


class part_processing(models.Model):
    pID = models.ForeignKey(part_list,on_delete=models.CASCADE)
    out_date = models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    req_form_no = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    vehicle_id = models.ForeignKey(customer_vehicle_info,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.req_form_no)+'-'+str(self.vehicle_id)