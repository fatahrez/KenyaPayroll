from django.forms import ModelForm
from django import forms
from pip._vendor.msgpack.fallback import xrange

from payroll.models import EmployeeModel
from payroll.utils import MonthYearWidget


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = "__all__"


class MonthForm(forms.Form):
    month = forms.CharField(label='Month', max_length=20)
