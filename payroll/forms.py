from django import forms
from django.forms import ModelForm

from payroll.models import EmployeeModel, Allowance


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"


class MonthForm(forms.Form):
    month = forms.CharField(label='Month', max_length=20)


class AllowanceForm(ModelForm):
    class Meta:
        model = Allowance
        fields = "__all__"
