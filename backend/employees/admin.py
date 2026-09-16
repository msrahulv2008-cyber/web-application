from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'full_name', 'department', 'designation', 'status', 'salary')
    search_fields = ('employee_code', 'full_name', 'email')
    list_filter = ('department', 'status')
