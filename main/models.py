from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class department(models.Model):
    name=models.CharField(max_length=30)
    address_city = models.CharField(max_length=30)
    address_district = models.CharField(max_length=30)
    contact=PhoneNumberField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address_city=models.CharField(max_length=30)
    address_district=models.CharField(max_length=30)
    contact=PhoneNumberField()
    salary=models.IntegerField()
    department_id=models.ForeignKey(department,on_delete=models.CASCADE)
    gender=models.BinaryField()
    joined_date=models.DateField()

    def __str__(self):
        return self.first_name +" "+self.last_name

class user(models.Model):
    user_id=models.OneToOneField(employee,on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    created_date=models.DateField()

    def __str__(self):
        return str(self.username)




