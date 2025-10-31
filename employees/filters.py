import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    Designation = django_filters.CharFilter(field_name='Designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method='filter_by_id_range',label='From EMP ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='To EMP ID')
    

    class Meta:
        model = Employee
        fields = ['Designation','emp_name','id_min','id_max']

    def filter_by_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset