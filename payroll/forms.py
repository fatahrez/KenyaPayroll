from django import forms
from django.forms import ModelForm
from monthyear.forms import MonthField

from payroll.models import EmployeeModel, Allowance


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"


class MonthForm(forms.Form):
    month = MonthField()


class AllowanceForm(ModelForm):
    class Meta:
        model = Allowance
        fields = "__all__"
