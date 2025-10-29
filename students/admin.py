from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','Name','Branch')
    search_fields = ('student_id',)

admin.site.register(Student,StudentAdmin)