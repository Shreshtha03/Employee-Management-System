from django.db import models
from django.core.validators import EmailValidator, RegexValidator

# Employee Table
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=100,
        unique=True,
        validators=[EmailValidator(message="Please enter a valid email address.")]
    )
    contact = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit phone number.')]
    )
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

# Department Table
class Department(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee} - {self.department_name}"

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"