from django.db import models
from django.contrib import admin
class Employees (models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=30)
    Emp_salary=models.IntegerField()
    Emp_email=models.EmailField()

class EmployeeAdmin (admin.ModelAdmin):
    list_display=('Emp_id','Emp_name','Emp_salary','Emp_email')
