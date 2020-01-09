from django.urls import path

from payroll import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/new/', views.create_employee, name='new_employee'),
    path('employees/', views.all_employees, name='all_employees'),
]
