from django.urls import path

from payroll import views

urlpatterns = [
    path('', views.index, name='index')
]