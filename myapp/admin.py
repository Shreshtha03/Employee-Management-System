from django.contrib import admin
from .models import Employee, Department

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact', 'date_of_joining')
    list_filter = ('date_of_joining',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('-date_of_joining',)

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'contact', 'date_of_joining')
        }),
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department_name')
    list_filter = ('department_name',)
    search_fields = ('employee_first_name', 'employee_last_name', 'department_name')
    ordering = ('employee',)

    fieldsets = (
        (None, {
            'fields': ('employee', 'department_name')
        }),
    )