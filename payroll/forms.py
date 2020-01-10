from django import forms
from django.forms import ModelForm

from payroll.models import EmployeeModel


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"


class MonthForm(forms.Form):
    month = forms.CharField(label='Month', max_length=20)
