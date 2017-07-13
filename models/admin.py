from django.contrib import admin
from .models import model_last, model_first, model_stock, customer_vehicle_info
# Register your models here.
admin.site.register(model_stock)
admin.site.register(model_first)
admin.site.register(model_last)
admin.site.register(customer_vehicle_info)