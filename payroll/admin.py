from django.contrib import admin
from payroll.models import EmployeeModel, PayrollModel, Allowance

# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(PayrollModel)
admin.site.register(Allowance)
