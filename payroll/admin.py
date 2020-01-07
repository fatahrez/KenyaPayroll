from django.contrib import admin
from payroll.models import EmployeeModel, PayrollModel

# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(PayrollModel)
