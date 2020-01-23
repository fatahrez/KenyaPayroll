from django.urls import path

from payroll import views

app_name = 'payroll'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('kra/', views.kra_view, name='kra'),
    path('kra/<str:month_year>/', views.kra_report, name='kraReport'),
    path('nssf/', views.nssf_view, name='nssf'),
    path('nhif/', views.nhif_view, name='nhif'),
    path('bank/', views.bank_reports, name='bankReports'),
    path('bank/<str:month_year>/', views.bank_report, name='bankReport'),
    path('bank/<str:month_year>/download/', views.bank_report_download, name='bankReport'),
    path('employees/new/', views.create_employee, name='new_employee'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/payroll/', views.generate_payroll, name='employee_payroll'),
    path('employees/<int:employee_id>/payroll/<str:month_year>/payslip', views.employee_payslip_pdf, name='employee_payslip'),
    path('employees/<int:employee_id>/edit', views.employee_update, name='employee_update'),
    path('employees/<int:employee_id>/delete', views.delete_employee, name='employee_delete'),
    path('allowances/', views.all_alllowances, name='allowances'),
    path('allowances/new/', views.create_allowance, name='create_allowance')
]
