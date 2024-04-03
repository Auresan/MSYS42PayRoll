"""shpayrollapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/<int:UID>', views.dashboard, name='dashboard'),
    path('', views.login, name='login'),
    path('employee_database/<int:UID>/', views.employee_database, name='employee_database'),
    path('add_employee/<int:UID>/', views.add_employee, name='add_employee'),
    path('generate_page/<int:UID>/', views.generate_page, name='generate_page'),
    path('employee_info/<int:UID>/<str:EID>/', views.employee_info, name='employee_info'),
    path('attendance_db/<int:UID>', views.attendance_db, name='attendance_db'),
    path('employee_attendance/<int:UID>', views.employee_attendance, name='employee_attendance'),
    path('encode_page/<int:UID>', views.encode_page, name='encode_page'),
    path('tax_module/<int:UID>', views.tax_module, name='tax_module'),
    path('payroll_breakdown/<int:UID>', views.payroll_breakdown, name='payroll_breakdown')
]