from django.contrib import admin
from .models import employee, user, department

admin.site.register(employee)
admin.site.register(user)
admin.site.register(department)
