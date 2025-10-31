import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    Designation = django_filters.CharFilter(field_name='Designation', lookup_expr='iexact')
    
    class Meta:
        model = Employee
        fields = ['Designation']