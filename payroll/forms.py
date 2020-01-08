from django.forms import ModelForm

from payroll.models import EmployeeModel


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'date_of_birth', 'residential_status',
                  'national_id',
                  'kra_pin', 'nssf_no', 'nhif_no', 'passport_photo', 'basic_salary', 'bank_account_name',
                  'bank_account_number', 'bank_branch',
                  'employee_job_number', 'date_of_employment', 'contract_end_date', 'job_title', 'employee_email',
                  'mobile_phone']
