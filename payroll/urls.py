from django.urls import path

from payroll import views

app_name = 'payroll'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('kra/', views.kra_view, name='kra'),
    path('nssf/', views.nssf_view, name='nssf'),
    path('nhif/', views.nhif_view, name='nhif'),
    path('new/', views.create_employee, name='new_employee'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/payroll/', views.generate_payroll, name='employee_payroll'),
    path('employees/<int:employee_id>/payroll/payslip', views.employee_payslip_pdf, name='employee_payslip')
]
