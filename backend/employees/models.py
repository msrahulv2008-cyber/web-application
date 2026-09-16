from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Employee(models.Model):
    STATUS_CHOICES = [('Active','Active'), ('On Leave','On Leave'), ('Resigned','Resigned')]
    DEPARTMENT_CHOICES = [(x, x) for x in ['Engineering','HR','QA','DevOps','Finance','Marketing','Sales','Support','Management']]
    phone_validator = RegexValidator(regex=r'^\d{10,15}$', message='Phone must contain 10 to 15 digits.')

    employee_code = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, validators=[phone_validator])
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    salary = models.FloatField(validators=[MinValueValidator(0.0)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.employee_code} - {self.full_name}'
