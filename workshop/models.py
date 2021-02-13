from django.db import models
import datetime
from vehicle_models.models import customer_vehicle_info
from main.models import employee
#from employee.models import

class job_records( models.Model ):
    job_order = models.CharField(max_length=250)
    job_done = models.CharField(max_length=500)
    vid = models.ForeignKey(customer_vehicle_info ,on_delete=models.CASCADE)
    date =models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    e_id = models.ForeignKey(employee,on_delete=models.CASCADE)


    def __str__( self ):
        return str(self.vid) + ' - ' + str(self.job_order)
