from django.urls import path

from payroll import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/new/', views.create_employee, name='new_employee'),
    path('employees/', views.all_employees, name='all_employees'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employees/<int:employee_id>/payroll/', views.generate_payroll, name='employee_payroll'),
    path('employees/<int:employee_id>/payroll/payslip', views.employee_payslip_pdf, name='employee_payslip')
]
