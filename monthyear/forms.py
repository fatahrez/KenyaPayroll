from django import forms
from monthyear.widgets import MonthSelectorWidget


class MonthField(forms.DateField):
    widget = MonthSelectorWidget
