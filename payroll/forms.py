from django.forms import ModelForm

from payroll.models import EmployeeModel


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"
