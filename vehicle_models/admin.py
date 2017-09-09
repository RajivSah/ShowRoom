from django.contrib import admin
from . import  models
# Register your vehicle_models here.

admin.site.register(models.Manufacturer)
admin.site.register(models.VehicleCategory)
admin.site.register(models.VehicleName)
admin.site.register(models.VehicleModels)
admin.site.register(models.ModelDetails)
admin.site.register(models.customer_vehicle_info)