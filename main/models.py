from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class department(models.Model):
    name=models.CharField(max_length=30)
    address_city = models.CharField(max_length=30)
    address_district = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class employee(models.Model):
    GEND_CHOICES=(
	("Male", ("Male")), 
	("Female", ("Female"))
	)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address_city=models.CharField(max_length=30)
    address_district=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    salary=models.IntegerField()
    department_id=models.ForeignKey(department,on_delete=models.CASCADE)
    Gender=models.CharField(max_length=10,choices=GEND_CHOICES)
    joined_date=models.DateField()

    def __str__(self):
        return self.first_name +" "+self.last_name

class user(models.Model):
    user_id=models.OneToOneField(employee,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    created_date=models.DateField()

    def __str__(self):
        return str(self.username)

    def authenticate(password_entered, username_entered):

        try:
             o=user.objects.get(username=username_entered, password=password_entered)
             return {'status':True, 'department':o.user_id.department_id.name}
        except:
             return False


