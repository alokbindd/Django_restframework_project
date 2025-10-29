from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','emp_name','Designation')
    search_fields = ('emp_id',)

admin.site.register(Employee,EmployeeAdmin)