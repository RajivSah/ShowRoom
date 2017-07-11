from django.db import models


class part_list(models.Model):
    part_id=models.CharField(max_length=30,unique=True)
    part_name=models.CharField(max_length=30)
    cost=models.IntegerField(default=0)
    available_quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.part_id

class applicable_model(models.Model):
    partId=models.ForeignKey(part_list,on_delete=models.CASCADE)
    applicable=models.CharField(max_length=30)

    def __str__(self):
        return self.partId

class part_stock(models.Model):
    part_id=models.ForeignKey(part_list,on_delete=models.CASCADE)
    entry_date=models.DateField()
    supplier=models.CharField(max_length=30)
    amount=models.IntegerField()
    remaining=models.IntegerField(default=0)

    def __str__(self):
        return self.part_id


