from rest_framework import serializers
from EmployeeApp.models import Departments, Employees

class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName','Department')