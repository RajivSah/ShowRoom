from django.contrib import admin
from . import  models
# Register your vehicle_models here.

admin.site.register(models.part_list)
admin.site.register(models.part_stock)
admin.site.register(models.applicable_model)