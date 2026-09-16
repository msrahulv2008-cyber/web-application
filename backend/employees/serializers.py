from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_phone(self, value):
        if not value.isdigit() or not 10 <= len(value) <= 15:
            raise serializers.ValidationError('Phone must contain 10 to 15 digits.')
        return value

class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
