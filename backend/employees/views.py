from rest_framework import viewsets, filters
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['employee_code', 'full_name', 'email', 'department', 'designation']
    ordering_fields = ['full_name', 'date_of_joining', 'salary', 'created_at']
    ordering = ['-created_at']
