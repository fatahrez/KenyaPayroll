import xlwt
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from weasyprint import HTML
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from payroll.forms import EmployeeForm, MonthForm, AllowanceForm
from payroll.models import EmployeeModel, PayrollModel, Allowance


# Create your views here.
class EmployeePayroll:
    basicSalary = 0
    gross_salary = 0
    taxable_income = 0
    nssf_deduction = 0
    nhif_deduction = 0
    payee = 0
    personal_relief = 1408
    total_tax_payable = 0
    net_salary = 0

    def __init__(self, basic_salary):
        self.basicSalary = basic_salary
        self.calculate_gross_salary()
        self.calculate_nssf()
        self.calculate_nhif()
        self.calculate_taxable_income()
        self.calculate_payee()
        self.calculate_tax_payable()
        self.calculate_net_salary()

    def calculate_gross_salary(self):
        gross_salary = self.basicSalary
        self.gross_salary = gross_salary

        return gross_salary

    def calculate_nssf(self):
        # Use old format instead of new
        nssf = 400
        self.nssf_deduction = nssf
        return nssf
        # if 0 < self.gross_salary <= 6000:
        #     nssf = 0.06 * self.gross_salary
        #     self.nssf_deduction = nssf
        #     return nssf
        # elif 6000 < self.gross_salary < 18000:
        #     remainder = self.gross_salary - 6000
        #     nssf = 6000 * 0.06 + remainder * 0.06
        #     self.nssf_deduction = nssf
        #     return nssf
        # elif self.gross_salary > 18000:
        #     nssf = 6000 * 0.06 + 12000 * 0.06
        #     self.nssf_deduction = nssf
        #     return nssf

    def calculate_nhif(self):
        if 0 <= self.gross_salary <= 5999:  # 0 - 5999
            nhif = 150
            self.nhif_deduction = nhif
            return nhif
        elif 6000 <= self.gross_salary <= 7999:  # 6000 - 7999
            nhif = 300
            self.nhif_deduction = nhif
            return nhif
        elif 8000 <= self.gross_salary <= 11999:
            nhif = 400
            self.nhif_deduction = nhif
            return nhif
        elif 12000 <= self.gross_salary <= 14999:  # 12000 - 14999
            nhif = 500
            self.nhif_deduction = nhif
            return nhif
        elif 15000 <= self.gross_salary < 19999:  # 15000 - 19999
            nhif = 600
            self.nhif_deduction = nhif
            return nhif
        elif 20000 <= self.gross_salary <= 24999:
            nhif = 750
            self.nhif_deduction = nhif
            return nhif
        elif 25000 <= self.gross_salary <= 29999:
            nhif = 850
            self.nhif_deduction = nhif
            return nhif
        elif 30000 <= self.gross_salary <= 34999:
            nhif = 900
            self.nhif_deduction = nhif
            return nhif
        elif 35000 <= self.gross_salary <= 39999:
            nhif = 950
            self.nhif_deduction = nhif
            return nhif
        elif 40000 <= self.gross_salary <= 44999:
            nhif = 1000
            self.nhif_deduction = nhif
            return nhif
        elif 45000 <= self.gross_salary <= 49999:
            nhif = 1100
            self.nhif_deduction = nhif
            return nhif
        elif 50000 <= self.gross_salary <= 59999:
            nhif = 1200
            self.nhif_deduction = nhif
            return nhif
        elif 60000 <= self.gross_salary <= 69999:
            nhif = 1300
            self.nhif_deduction = nhif
            return nhif
        elif 70000 <= self.gross_salary <= 79999:
            nhif = 1400
            self.nhif_deduction = nhif
            return nhif
        elif 80000 <= self.gross_salary <= 89999:
            nhif = 1500
            self.nhif_deduction = nhif
            return nhif
        elif 90000 <= self.gross_salary <= 99999:
            nhif = 1600
            self.nhif_deduction = nhif
            return nhif
        elif self.gross_salary >= 100000:
            nhif = 1700
            self.nhif_deduction = nhif
            return nhif

    def calculate_taxable_income(self):
        nti = self.gross_salary - self.nssf_deduction
        self.taxable_income = nti
        return nti

    def calculate_payee(self):
        tier1 = 12298
        tier2 = 11587
        tier3 = 11587
        tier4 = 11587

        if self.taxable_income <= 12298:
            tax = self.taxable_income * 0.1
            self.payee = tax
            return tax
        elif 12299 <= self.taxable_income <= 23885:
            remainder = self.taxable_income - 12298
            tax = tier1 * 0.1 + 0.15 * remainder
            self.payee = tax
            return tax
        elif 23886 <= self.taxable_income <= 35472:
            remainder = self.taxable_income - tier1 - tier2
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (0.2 * remainder)
            self.payee = tax
            return tax
        elif 35473 <= self.taxable_income <= 47059:
            remainder = self.taxable_income - tier1 - tier2 - tier3
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (tier3 * 0.2) + (0.25 * remainder)
            self.payee = tax
            return tax
        elif self.taxable_income >= 47059:
            remainder = self.taxable_income - tier1 - tier2 - tier3 - tier4
            tax = (tier1 * 0.1) + (tier2 * 0.15) + (tier3 * 0.2) + (0.25 * tier4) + (0.3 * remainder)
            self.payee = tax
            return tax

    def calculate_tax_payable(self):
        tax_payable = self.payee - self.personal_relief
        self.total_tax_payable = tax_payable
        return tax_payable

    def calculate_net_salary(self):
        net_sal = self.taxable_income - (self.nhif_deduction + self.total_tax_payable)
        self.net_salary = net_sal
        return net_sal


@login_required
def index(request):
    employees = EmployeeModel.objects.all()
    employees_count = employees.count()

    allowances = Allowance.objects.all()
    allowance_count = allowances.count()

    bank_report_count = PayrollModel.objects.order_by('month_year').distinct('month_year').count()

    return render(request, 'payroll/index.html',
                  {'employees_count': employees_count, 'allowance_count': allowance_count,
                   'bank_report_count': bank_report_count})


def employees(request):
    employees = EmployeeModel.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully")
        else:
            messages.error(request, "Error adding employee")
    else:
        form = EmployeeForm()
    return render(request, 'payroll/employees.html', {'employees': employees, 'employee_form': form})


def nhif_view(request):
    months = PayrollModel.objects.order_by('month_year').distinct('month_year')
    return render(request, 'payroll/nhif.html', {'months': months})


def nssf_view(request):
    months = PayrollModel.objects.order_by('month_year').distinct('month_year')
    return render(request, 'payroll/nssf.html', {'months': months})


def nssf_report(request, month_year):
    payroll = PayrollModel.objects.filter(month_year=month_year)
    nssf_total = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('nssf_deduction'))
    grosspay_total = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('gross_pay'))
    return render(request, 'payroll/nssf_report.html', {'month': month_year, 'payroll': payroll,
                                                        'nssf_total': nssf_total['nssf_deduction__sum'],
                                                        'grosspay_total': grosspay_total['gross_pay__sum']})


def kra_view(request):
    months = PayrollModel.objects.order_by('month_year').distinct('month_year')
    return render(request, 'payroll/kra.html', {'months': months})


def kra_report(request, month_year):
    payroll = PayrollModel.objects.filter(month_year=month_year)
    gross_pay_total = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('gross_pay'))['gross_pay__sum']
    nssf_contribution_total = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('nssf_deduction'))
    tax_chargable = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('payee'))['payee__sum']
    personal_relief = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('personal_relief'))
    total_tax = PayrollModel.objects.filter(month_year=month_year).aggregate(Sum('total_tax'))['total_tax__sum']
    return render(request, 'payroll/kra_report.html', {'payroll': payroll, 'month': month_year,
                                                       'gross_pay_total': gross_pay_total,
                                                       'nssf_deduction': nssf_contribution_total['nssf_deduction__sum'],
                                                       'tax_chargable': tax_chargable,
                                                       'personal_relief': personal_relief['personal_relief__sum'],
                                                       'total_tax': total_tax})


def bank_reports(request):
    payroll = PayrollModel.objects.order_by('month_year').distinct('month_year')
    return render(request, 'payroll/bank_reports.html', {'payroll': payroll})


def bank_report(request, month_year):
    payroll = PayrollModel.objects.filter(month_year=month_year)
    return render(request, 'payroll/bank_report.html', {'payroll': payroll, 'month': month_year})


def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')

    else:
        form = EmployeeForm()

    return render(request, 'payroll/employee.html', {'employee_form': form})


def employee_detail(request, employee_id):
    employee = get_object_or_404(EmployeeModel, pk=employee_id)
    return render(request, 'payroll/employee_detail.html', {'employee': employee})


def generate_payroll(request, employee_id):
    if request.method == 'POST':
        form = MonthForm(request.POST)

        if form.is_valid():
            employee = EmployeeModel.objects.get(pk=employee_id)
            calculate_payroll = EmployeePayroll(int(employee.basic_salary))
            payroll = PayrollModel.objects.create(employee_id_id=employee_id)
            payroll.month_year = form.cleaned_data['month']
            payroll.gross_pay = calculate_payroll.basicSalary
            payroll.nssf_deduction = calculate_payroll.nssf_deduction
            payroll.nhif_deduction = calculate_payroll.nhif_deduction
            payroll.payee = calculate_payroll.payee
            payroll.personal_relief = calculate_payroll.personal_relief
            payroll.total_tax = calculate_payroll.total_tax_payable
            payroll.net_salary = calculate_payroll.net_salary
            payroll.save()
            return HttpResponseRedirect('/')
    else:
        form = MonthForm()

    payroll = PayrollModel.objects.filter(employee_id_id=employee_id)

    return render(request, 'payroll/calculate_payroll_employee.html', {'form': form, 'payrolls': payroll})


def employee_payslip_pdf(request, employee_id, month_year):
    payroll = PayrollModel.objects.filter(employee_id_id=employee_id, month_year=month_year).values()
    # pre_total = payroll.first().net_salary - payroll.first().nhif_deduction
    html_string = render_to_string('payroll/payslip_pdf_template.html', {'payroll': payroll.first()})

    html = HTML(string=html_string).write_pdf(target='/tmp/mypayslip.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypayslip.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypayslip.pdf"'
        return response
    return response


def create_allowance(request):
    if request.method == 'POST':
        form = AllowanceForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/allowances')
    else:
        form = AllowanceForm()

    return render(request, 'payroll/allowance.html', {'form': form})


def all_alllowances(request):
    allowances = Allowance.objects.all()

    return render(request, 'payroll/allowances.html', {'allowances': allowances})


def employee_edit(request, employee_id):
    employee = EmployeeModel.objects.get(id=employee_id)
    return render(request, 'employee_update_form.html', {'employee': employee})


def employee_update(request, employee_id):
    employee = EmployeeModel.objects.get(id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("/employees")
    return render(request, 'employee_update_form.html', {'employee': employee})


def delete_employee(request, employee_id):
    employee = EmployeeModel.objects.get(id=employee_id)
    employee.delete()
    return HttpResponseRedirect("/employees")


def bank_report_download(request, month_year):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="bank_report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Bank Report')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['EmpNo', 'EmpName', 'Bank Name', 'Account No.', 'Net Pay', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = PayrollModel.objects.filter(month_year=month_year).values_list('employee_id__employee_personal_number',
                                                                          'employee_id__first_name',
                                                                          'employee_id__bank',
                                                                          'employee_id__bank_account_number',
                                                                          'net_salary')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


def kra_report_download(request, month_year):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="kra_report.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('KRA Report')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Employee Pin', 'Employee Name', 'Total Cash', 'Total Gross Pay', 'NSSF Contribution', 'chargable pay',
               'Tax Chargable', 'Personal Relief', 'P.A.Y.E Tax']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = PayrollModel.objects.filter(month_year=month_year). \
        distinct('employee_id').values_list('employee_id__kra_pin',
                                            'employee_id__first_name',
                                            'employee_id__payrollmodel__gross_pay',
                                            'employee_id__payrollmodel__gross_pay',
                                            'employee_id__payrollmodel__nssf_deduction',
                                            'employee_id__payrollmodel__gross_pay',
                                            'employee_id__payrollmodel__payee',
                                            'employee_id__payrollmodel__personal_relief',
                                            'employee_id__payrollmodel__total_tax')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
