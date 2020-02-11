from django.db import models

# Create your models here.
from monthyear.models import MonthField


class EmployeeModel(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    RESIDENTIAL_OPTIONS = (
        ('R', 'Resident'),
        ('NR', 'Non-Resident')
    )

    CONTRACT_OPTIONS = (
        ('P', 'Permanent'),
        ('T', 'Temporary')
    )

    first_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, null=True)
    date_of_birth = models.DateField(null=True)
    residential_status = models.CharField(max_length=2, choices=RESIDENTIAL_OPTIONS, null=True)
    national_id = models.CharField(max_length=10, unique=True, null=True)
    kra_pin = models.CharField(max_length=11, unique=True, null=True)
    nssf_no = models.CharField(max_length=15, unique=True, null=True)
    nhif_no = models.CharField(max_length=15, unique=True, null=True)
    passport_photo = models.ImageField(blank=True, null=True)
    basic_salary = models.CharField(max_length=15, null=True)
    allowances = models.ManyToManyField('Allowance', blank=True)
    bank = models.CharField(max_length=50, null=True)
    bank_account_name = models.CharField(max_length=255, null=True)
    bank_account_number = models.CharField(max_length=35, null=True)
    bank_branch = models.CharField(max_length=40, null=True)
    employee_personal_number = models.CharField(max_length=50, null=True)
    date_of_employment = models.DateField(null=True)
    contract_type = models.CharField(choices=CONTRACT_OPTIONS, max_length=1, null=True)
    job_title = models.CharField(max_length=50, null=True)
    employee_email = models.EmailField(unique=True, null=True)
    mobile_phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.last_name


class PayrollModel(models.Model):
    month_year = MonthField("Month Value", help_text="some help...", null=True)
    gross_pay = models.IntegerField(null=True)
    nssf_deduction = models.IntegerField(null=True)
    nhif_deduction = models.IntegerField(null=True)
    payee = models.IntegerField(null=True)
    personal_relief = models.IntegerField(null=True)
    total_tax = models.IntegerField(null=True)
    net_salary = models.IntegerField(null=True)
    employee_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.employee_id.last_name

    def __unicode__(self):
        return unicode(self.month_year)


class Allowance(models.Model):
    allowance_name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.allowance_name
