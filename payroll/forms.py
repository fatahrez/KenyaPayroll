from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm
from monthyear.forms import MonthField

from payroll.models import EmployeeModel, Allowance
from crispy_forms.layout import Field, Layout, Div, ButtonHolder, Submit


class EmployeeForm(ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    date_of_employment = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(Field('first_name'), css_class='col-md-4', ),
                Div(Field('last_name'), css_class='col-md-4', ),
                Div(Field('middle_name'), css_class='col-md-4', ),
                Div(Field('gender'), css_class='col-md-4', ),
                Div(Field('date_of_birth'), css_class='col-md-4', ),
                Div(Field('residential_status'), css_class='col-md-4', ),
                Div(Field('national_id'), css_class='col-md-4', ),
                Div(Field('allowances'), css_class='col-md-4', ),
                css_class='row',
            ),
            Div(
                Div(Field('nssf_no'), css_class='col-md-4', ),
                Div(Field('nhif_no'), css_class='col-md-4', ),
                Div(Field('kra_pin'), css_class='col-md-4', ),
                Div(Field('passport_photo'), css_class='col-md-4', ),
                Div(Field('basic_salary'), css_class='col-md-4', ),
                Div(Field('bank'), css_class='col-md-4', ),
                Div(Field('bank_account_name'), css_class='col-md-4', ),
                Div(Field('bank_account_number'), css_class='col-md-4', ),
                css_class='row',
            ),
            Div(
                Div(Field('bank_branch'), css_class='col-md-4', ),
                Div(Field('employee_personal_number'), css_class='col-md-4', ),
                Div(Field('date_of_employment'), css_class='col-md-4', ),
                Div(Field('contract_type'), css_class='col-md-4', ),
                Div(Field('job_title'), css_class='col-md-4', ),
                Div(Field('employee_email'), css_class='col-md-4', ),
                Div(Field('mobile_phone'), css_class='col-md-4', ),
                css_class='row',
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='button white')
            )
        )
        super(EmployeeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EmployeeModel
        fields = "__all__"


class MonthForm(forms.Form):
    month = MonthField()


class AllowanceForm(ModelForm):
    class Meta:
        model = Allowance
        fields = "__all__"



